import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv('heart.csv')
# print(df.head())

# sns.countplot(data=df,x='target')
# plt.show()

# sns.pairplot(df[['age','trestbps','chol','thalach','target']],hue='target')
# plt.show()

# sns.heatmap(df.corr(),annot=True)
# plt.show()

X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler =  StandardScaler()
sc_Xtrain = scaler.fit_transform(X_train)
sc_Xtest = scaler.transform(X_test)

model = LogisticRegression()
model.fit(sc_Xtrain,y_train)

y_pred = model.predict(sc_Xtest)

accuracy = accuracy_score(y_test,y_pred)
print(accuracy)
