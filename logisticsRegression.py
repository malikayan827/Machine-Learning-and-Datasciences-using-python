import pandas as pd
from matplotlib import pyplot as plt
df=pd.read_csv('insurance_data.csv')
print(df.head())

plt.scatter(df.age,df.bought_insurance,marker='+',color='red')
# plt.show()
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(df[['age']],df.bought_insurance,train_size=0.1)
print(X_test)
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(X_train,y_train)
print(model.predict(X_test))
print(model.score(X_test,y_test))
print(model.predict_proba(X_test))

