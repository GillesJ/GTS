#!/usr/bin/env python3
'''
Exploratory Data Analysis on parsed data in /data/
Get some stats to compare datasets.

eda.py in GTS
2/2/21 Copyright (c) Gilles Jacobs
'''
from pathlib import Path
from collections import Counter
from itertools import groupby
import json
import numpy as np
import pandas as pd
from copy import deepcopy

def basic_stats(data):

    # count the B tags in triples to get opinion term count
    opi_tags = [[t.split("\\")[-1] for t in inst["opinion_tags"].split(" ")] for sen in data for inst in sen["triples"]]
    opi_c = sum(Counter(tags)["B"] for tags in opi_tags)

    counts = {
        "sentences_n": len(data),
        "target_n": sum(len(inst["triples"]) for inst in data),
        "opinion_n": opi_c,
    }
    # count polarities
    pol_c = Counter(triple["sentiment"] for inst in data for triple in inst["triples"])
    for k, v in pol_c.items():
        counts[f"{k}_n"] = v
        counts[f"{k}_pct"] = round(v / sum(pol_c.values()) * 100.0, 1)

    return counts

if __name__ == "__main__":

    data_all_dir = "../data/"
    data_all_dp = Path(data_all_dir)

    exclude = ["sentivent-devproto"]

    all_splits = [fp for fp in data_all_dp.rglob("**/*.json") if fp.stem in ["train", "test", "dev"] and \
                  not fp.parent.stem in exclude]

    dset_key = lambda x: x.parts[2:-1]
    data_unrolled = []
    for dataset_name, dataset_fps in groupby(sorted(all_splits, key=dset_key), dset_key):
        print(f"-----\nstats for {'/'.join(dataset_name).upper()}:")
        all_stats = []
        for split_fp in dataset_fps:

            with open(split_fp, "rt") as json_in:
                split_data = json.load(json_in)
            stats = basic_stats(split_data)
            print(f"{split_fp.stem}: {stats}")
            all_stats.append(stats)

            # unroll sentence-level data to target-level
            for inst in split_data:
                triple_unrolled = [triple for triple in inst["triples"]]
                for trp in triple_unrolled:
                    triple_data = {k: v for k, v in inst.items() if k != "triples"}
                    triple_data.update(trp)
                    triple_data["split"] = split_fp.stem
                    triple_data["dataset"] = "-".join(dataset_name)
                    tag_a_c = Counter(toklab.split('\\')[-1] + "_A" for toklab in triple_data["target_tags"].split(" "))
                    tag_o_c = Counter(toklab.split('\\')[-1] + "_O" for toklab in triple_data["opinion_tags"].split(" "))
                    tag_a_c.update({"B_A": 0, "I_A": 0, "O_A": 0})
                    tag_o_c.update({"B_O": 0, "I_O": 0, "O_O": 0})
                    triple_data.update(tag_a_c)
                    triple_data.update(tag_o_c)
                    data_unrolled.append(triple_data)

        all_stats = sum([Counter(d) for d in all_stats], Counter())
        for pol in ["negative", "positive", "neutral"]: # get polarity percentages over whole set
            all_stats[f"{pol}_pct"] = round(100*all_stats[f"{pol}_n"]/all_stats["target_n"],1)
        print(f"all: {dict(all_stats)}")

    df_all = pd.DataFrame(data_unrolled)

    df_ponti = df_all[~df_all["dataset"].str.contains("sentivent")]
    df_senti = df_all[df_all["dataset"].str.contains("sentivent")]

    for k, df in [("Ponti", df_ponti), ("Senti", df_senti)]:
        sen_len = pd.Series(df["sentence"].unique()).apply(lambda x: len(x.split(" ")))
        print(f"{k} sentence token length:\t{sen_len.mean().round(1)} avg\t{sen_len.min()} min\t{sen_len.max()} max")

    pass