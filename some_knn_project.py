import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, roc_auc_score, auc
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV

df = pd.read_csv('KNN_Project_Data.csv')
print(df.head())

# sns.pairplot(data=df,hue='TARGET CLASS')
# plt.show()

X = df.drop('TARGET CLASS',axis=1)
y = df['TARGET CLASS']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

pipeline = make_pipeline(StandardScaler(),KNeighborsClassifier(n_neighbors=1))
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

param_grid = {'kneighborsclassifier__n_neighbors': range(1, 40)}

grid = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy')

error_rate = []
for params in grid.get_params()['param_grid']['kneighborsclassifier__n_neighbors']:
    grid.set_params(param_grid={'kneighborsclassifier__n_neighbors': [params]})
    grid.fit(X_train, y_train)
    y_pred = grid.predict(X_test)
    error = 1 - accuracy_score(y_test, y_pred)
    error_rate.append(error)

# sns.lineplot(x=range(1, 40),y=error_rate)
# plt.show()

pipeline = make_pipeline(StandardScaler(),KNeighborsClassifier(n_neighbors=33))
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))