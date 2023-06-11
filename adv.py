import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, roc_auc_score, auc

df = pd.read_csv('advertising.csv')

# print(df.head())
#
# print(df.info())
# print(df.describe())

# sns.histplot(data=df,x='Age'])
# plt.show()

# sns.jointplot(data=df,x='Age',y='Area Income')
# plt.show()

# sns.jointplot(data=df,x='Age',y='Daily Time Spent on Site',color='green',kind='kde')
# plt.show()

# sns.jointplot(data=df,x='Daily Time Spent on Site',y='Daily Internet Usage')
# plt.show()

# sns.pairplot(data=df,hue='Clicked on Ad')
# plt.show()

X = df.loc[:, ['Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage', 'Male']]
y = df['Clicked on Ad']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print(accuracy_score(y_test, y_pred))

print(confusion_matrix(y_test, y_pred))

fpr, tpr, thresholds = roc_curve(y_test, y_pred)

auc = roc_auc_score(y_test, y_pred)

auc_score = roc_auc_score(y_test, y_pred)

sns.set(style='whitegrid')
plt.figure(figsize=(8, 6))
sns.lineplot(x=[0, 1], y=[0, 1], color='red', linestyle='--', label='Random Guessing')
sns.lineplot(x=fpr, y=tpr, label='ROC Curve (AUC = %0.2f)' % auc_score)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend()
plt.show()

print(classification_report(y_test, y_pred))