import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
def nan(df):
    na = df.isna().sum().sum()
    if na != 0 :
        print(f"결측값 발견 total : {na}")
        mode = " "
        while(mode != "A" or "MA" or "MI" or "ME" or " N"):
            mode = str(input("결측값 처리 방법을 선택하시오.\n(A : Mean,  Ma : Max,  Mi : Min,  Me : Median,  N : None\n=> ")).upper()
            if(mode == "A"): df.fillna(df.Mean())
            elif(mode == "MA"): df.fillna(df.Max())
            elif(mode == "MI"): df.fillna(df.Min())
            elif(mode == "ME"): df.fillna(df.Median())
            else: 
                print("다시 입력하세요!!") 
                break
    else:
        print("결측값 없음")
    return df

def data_size(df):
    X = df.iloc[:,:-1]
    y = df.iloc[:,-1]
    size = float(input("테스트 사이즈를 입력하세요\n=> "))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = size, random_state = 42, stratify = y)
    return X_train, X_test, y_train, y_test
    
def scaler(X_train, X_test):
    mode = ""
    while(mode != ("M" or "S" or "N")):
        mode = str(input("스케일링 방법을 선택하시오\n(M : Minmax,  S : Standard,  N : None\n=> ")).upper()
        if mode == "M": ss = MinMaxScaler()
        elif mode == "S": ss = StandardScaler()
        elif mode == "N": break
        ss.fit(X_train)
        X_train = ss.transform(X_train)
        X_test = ss.transform(X_test)
        print(mode)
    return X_train, X_test