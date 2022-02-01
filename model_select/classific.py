from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

def C():
    mode=""
    while(mode != ("LR" or "LS" or "LB" or "KNN" or "DT")):
        mode = str(input("분류 모델을 선택하세요.\n(LR : linearRegression,  DT : decision_tree, LS : linear_svm, RS : rbf_svm, KNN : kneighbors\n=> ")).upper()
        if mode == "LR": model = LR(); break
        elif mode == "LS": model = LS(); break
        elif mode == "DT": model = DT(); break
        elif mode == "RS": model = RS(); break
        elif mode == "KNN": model = KNN(); break
    return model

def LR():   #linear_regression
    print("선형회귀에 필요한 파라미터는 ----입니다.")
    model = LinearRegression(n_jobs=-1)
    return model    
def DT():   #Decision_tree
    print("결정트리에 필요한 파라미터는 max_depth, criterion입니다.")
    depth, crite = str(input("파라미터를 입력해주세요. ex) 100 gini\n=> ")).split(" ")
    model = DecisionTreeClassifier(max_depth=int(depth), criterion=crite,random_state=42)
    return model
def LS():   #linear_svm
    print("서포트 벡터머신(선형)에 필요한 파라미터는 C입니다.")
    C = float(input("파라미터를 입력해즈세요. ex)0.001\n=> "))
    model = SVC(kernel = "linear", C = C,random_state = 42)
    return model
def RS():   #rbf_svm
    print("서포트 벡터머신(커널)에 필요한 파라미터는 C, gamma 입니다.")
    C, gamma = str(input("파라미터를 입력해주세요. ex)0.001 0.001\n=> "))
    model = SVC(kernel = "rbf", C = float(C), gamma = float(gamma), random_state = 42)
    return model
def KNN():  #Kneighbors
    print("최근접이웃에 필요한 파라미터는 n_neighbors입니다.")
    k = int(input("파라미터를 입력해주세요. ex) 3(홀수)\n=> "))
    model = KNeighborsClassifier(n_neighbors = k, n_jobs = -1)
    return model