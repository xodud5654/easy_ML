from . import classific as Cf
from . import ensemble as Es
from . import regression as Rg

def model_setting():
    print("모델 선택전 원하는 머신러닝 기법을 선택하시오")
    mode = str(input("C : classific,  R : regression,  E : ensemble\n=> ")).upper()
    if mode == "C": model = Cf.C()
    elif mode == "R": a=0
    elif mode == "E": model = Es.E()
    return model