# Experiment notes: Pilot

Training runs:

--max_sequence_len 100 -> OOM

1. CUDA_VISIBLE_DEVICES=1 python main.py --task triplet --mode train --dataset sentivent-devproto-no-empty --max_sequence_len 80

best epoch: 81	best dev triplet f1: 0.14527

Evaluation on testset:
Aspect term	P:0.54751	R:0.56279	F1:0.55505
Opinion term	P:0.28881	R:0.34783	F1:0.31558
triplet	P:0.16129	R:0.15326	F1:0.15717

2. CUDA_VISIBLE_DEVICES=1 python main.py --task triplet --mode train --dataset sentivent-devproto-no-empty --max_sequence_len 90

best epoch: 95  best dev triplet f1: 0.14944

Evaluation on testset:
Aspect term     P:0.54585       R:0.58140       F1:0.56306
Opinion term    P:0.24752       R:0.32609       F1:0.28143
triplet P:0.13380       R:0.14559       F1:0.13945

3. CUDA_VISIBLE_DEVICES=1 python main.py --task triplet --mode train --dataset sentivent-devproto-no-empty --max_sequence_len 100 --batch_size 16

best epoch: 71  best dev triplet f1: 0.15789

Evaluation on testset:
Aspect term     P:0.56422       R:0.57209       F1:0.56813
Opinion term    P:0.28346       R:0.31304       F1:0.29752
triplet P:0.17826       R:0.15709       F1:0.16701

4. CUDA_VISIBLE_DEVICES=1 python main.py --task triplet --mode train --dataset sentivent-devproto-no-empty --max_sequence_len 100 --batch_size 16 --learning_rate 1e-5 --epochs 200

best epoch: 105 best dev triplet f1: 0.13226

Evaluation on testset:
Aspect term     P:0.49412       R:0.58605       F1:0.53617
Opinion term    P:0.29368       R:0.34348       F1:0.31663
triplet P:0.13971       R:0.14559       F1:0.14259

5. CUDA_VISIBLE_DEVICES=1 python main.py --task triplet --mode train --dataset sentivent-devproto-no-empty --max_sequence_len 100 --batch_size 16 --learning_rate 2e-5 --epochs 200

best epoch: 191 best dev triplet f1: 0.16456

Evaluation on testset:
Aspect term     P:0.52675       R:0.59535       F1:0.55895
Opinion term    P:0.29592       R:0.37826       F1:0.33206
triplet P:0.14626       R:0.16475       F1:0.15495

6. CUDA_VISIBLE_DEVICES=1 python main.py --task triplet --mode train --dataset sentivent-devproto-no-empty --max_sequence_len 100 --batch_size 8 --learning_rate 2e-5 --epochs 200

best epoch: 80  best dev triplet f1: 0.17391

Evaluation on testset:
Aspect term     P:0.54959       R:0.61860       F1:0.58206
Opinion term    P:0.29110       R:0.36957       F1:0.32567
triplet P:0.15194       R:0.16475       F1:0.15809

7. CUDA_VISIBLE_DEVICES=1 python main.py --task triplet --mode train --dataset sentivent-devproto-no-empty --max_sequence_len 100 --batch_size 6 --learning_rate 1e-5 --epochs 200

best epoch: 144 best dev triplet f1: 0.16584


Evaluation on testset:
Aspect term     P:0.53689       R:0.60930       F1:0.57081
Opinion term    P:0.26897       R:0.33913       F1:0.30000
triplet P:0.12903       R:0.13793       F1:0.13333

8.  CUDA_VISIBLE_DEVICES=1 python main.py --task triplet --mode train --dataset sentivent-devproto-no-empty --max_sequence_len 100 --batch_size 6 --learning_rate 2e-5 --epochs 200

best epoch: 48  best dev triplet f1: 0.15537


Evaluation on testset:
Aspect term     P:0.50195       R:0.60000       F1:0.54661
Opinion term    P:0.31034       R:0.35217       F1:0.32994
triplet P:0.13962       R:0.14176       F1:0.14068

9. CUDA_VISIBLE_DEVICES=1 python main.py --task triplet --mode train --dataset sentivent-devproto-no-empty --max_sequence_len 100 --batch_size 8 --learning_rate 1e-5 --epochs 200 

best epoch: 196 best dev triplet f1: 0.16014

Evaluation on testset:
Aspect term     P:0.51793       R:0.60465       F1:0.55794
Opinion term    P:0.29885       R:0.33913       F1:0.31772
triplet P:0.16538       R:0.16475       F1:0.16507

10. CUDA_VISIBLE_DEVICES=1 python main.py --task triplet --mode train --dataset sentivent-devproto-no-empty --max_sequence_len 100 --batch_size 8 --learning_rate 2e-5 --epochs 200 -nhops 2

best epoch: 119 best dev triplet f1: 0.16867


Evaluation on testset:
Aspect term     P:0.53604       R:0.55349       F1:0.54462
Opinion term    P:0.26740       R:0.31739       F1:0.29026
triplet P:0.16049       R:0.14943       F1:0.15476

11. CUDA_VISIBLE_DEVICES=1 python main.py --task triplet --mode train --dataset sentivent-devproto-no-empty --max_sequence_len 100 --batch_size 8 --learning_rate 2e-5 --epochs 200 --nhops 3

Aspect term     P:0.56667       R:0.56432       F1:0.56549
Opinion term    P:0.27181       R:0.28622       F1:0.27883
triplet P:0.17623       R:0.14238       F1:0.15751

best epoch: 75  best dev triplet f1: 0.16118


Evaluation on testset:
Aspect term     P:0.50000       R:0.57209       F1:0.53362
Opinion term    P:0.26736       R:0.33478       F1:0.29730
triplet P:0.15909       R:0.16092       F1:0.16000

11. CUDA_VISIBLE_DEVICES=1 python main.py --task triplet --mode train --dataset sentivent-devproto-no-empty --max_sequence_len 100 --epochs 100 --nhops 2 --batch_size 12
