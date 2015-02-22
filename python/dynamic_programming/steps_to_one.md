
```
$ time -p python dp.steps.py 1000
Num: 1000, NumSteps: 9, Steps: ((1000 - 1) / 3 / 3 / 3 - 1) / 2 / 2 / 3 / 3
real 0.02
user 0.01
sys 0.00

$ time -p python dp.steps.py 10000
Num: 10000, NumSteps: 14, Steps: (((((10000 - 1) / 3 / 3 - 1) / 3 - 1) / 3 / 3 - 1) / 2 / 2 - 1) / 3 / 3
real 0.03
user 0.02
sys 0.00

$ time -p python dp.steps.py 100000
Num: 100000, NumSteps: 18, Steps: (((((100000 / 2 / 2 / 2 / 2 - 1) / 3 - 1) / 3 - 1) / 3 / 3 - 1) / 2 / 2 - 1) / 2 / 3 / 3
real 0.15
user 0.13
sys 0.01

$ time -p python dp.steps.py 1000000
Num: 1000000, NumSteps: 19, Steps: ((1000000 / 2 / 2 / 2 / 2 / 2 / 2 - 1) / 2 / 2 / 2 / 3 / 3 - 1) / 2 / 2 / 2 / 3 / 3 / 3
real 1.26
user 1.21
sys 0.05

$ time -p python dp.steps.py 10000000
Num: 10000000, NumSteps: 22, Steps: ((((((10000000 - 1) / 3 / 3 - 1) / 2 / 3 - 1) / 2 / 3 / 3 - 1) / 3 / 3 / 3 / 3 - 1) / 2 / 3 / 3 - 1) / 2 / 3
real 12.63
user 12.01
sys 0.61
```
