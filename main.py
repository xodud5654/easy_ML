from model_preprocess import load,preprocess
from model_select import model_set
from predicts import predict

def play():
    X_train, X_test, y_train, y_test = load.loading()
    print("next")
    answer="Y"
    while(answer=="Y"):
        model = model_set.model_setting()
        print("next")
        predict.pred(model,X_train, X_test, y_train, y_test)
        answer = str(input("계속하시겠습니까?(Y|N)\n=> ")).upper()
    print("수고하셨습니다.")
    
play()