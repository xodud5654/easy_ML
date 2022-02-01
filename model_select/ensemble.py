from joblib import MemorizedResult
from sklearn.ensemble import RandomForestClassifier, VotingClassifier, StackingClassifier
from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier

def E():
    while(mode != ("LR" or "LS" or "LB" or "KNN")):
        mode = str(input("앙상블 모델을 선택하세요.\n\
            (RF : RandomForest,  VT : Voting,  ST : Stacking, BG : Bagging,  AB : Adaboost\n=> ")).upper()
        if mode == "RF": model = RF()
        elif mode == "VT": model = VT()
        elif mode == "ST": model = ST()
        elif mode == "BG": model = BG()
        elif mode == "AB": model = AB()
    return model
def RF():
    print("랜덤포레스트에 필요한 파라미터는 max_depth, Tree개수입니다.")
    depth, n = str(input("파라미터를 입력해주세요. ex) 100 100\n=> ")).split(" ")
    model = RandomForestClassifier(n_estimators = int(n), max_depth = int(depth), random_state = 42, n_jobs = -1)
    return model 

def VT():
    
    return model

def ST():
    
    return model

def BG():
    
    return model

def AB():
    
    return model