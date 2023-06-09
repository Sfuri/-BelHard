import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, roc_auc_score, auc

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

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(accuracy_score(y_test, y_pred))

print(confusion_matrix(y_test, y_pred))

fpr, tpr, thresholds = roc_curve(y_test, y_pred)

auc = roc_auc_score(y_test, y_pred)
print("AUC-ROC: {:.3f}".format(auc))

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
