from sklearn.metrics import recall_score, roc_auc_score, confusion_matrix, accuracy_score

def pred(model,X_train,X_test,y_train,y_test):
    print("running...")
    model.fit(X_train,y_train)
    y_test_pred = model.predict(X_test)
    print("train complete")
    print(accuracy_score(y_test,y_test_pred))