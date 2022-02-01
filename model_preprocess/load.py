from . import preprocess as pp
import pandas as pd

def file_load():
    path = str(input("파일 업로드\n=> "))
    df = pd.read_csv(path)
    return df 

def loading():
    df = file_load()
    df = pp.nan(df)
    X_train, X_test, y_train, y_test = pp.data_size(df)
    X_train, X_test = pp.scaler(X_train, X_test)
    print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
    return X_train, X_test, y_train, y_test
