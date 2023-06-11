import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import  confusion_matrix, classification_report
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV

df = pd.read_csv('sonar.all-data.csv')
# print(df.head())

labels = df['Label']
df = df.drop('Label', axis=1)
# print(df.head())

# sns.heatmap(df.corr(),cmap='coolwarm')
# plt.show()

df['Label'] = labels
df['Label'] = df['Label'].replace({'R': 1, 'M': 0})

correlation = df.drop('Label', axis=1).corrwith(df['Label'])
sorted_correlation = correlation.abs().sort_values(ascending=False)
top_5_freq = sorted_correlation.index[:5]
# print(top_5_freq)

X = df.drop('Label', axis=1)
y = df['Label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

pipeline = make_pipeline(StandardScaler(), KNeighborsClassifier())
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

grid = GridSearchCV(pipeline, {'kneighborsclassifier__n_neighbors': range(1, 30)}, cv=5, scoring='accuracy')
# print(grid)

grid.fit(X_train, y_train)
print(grid.best_params_)

res = grid.cv_results_['mean_test_score']
print(res)
k_values = grid.cv_results_['param_kneighborsclassifier__n_neighbors']

# sns.lineplot(x=k_values,y=res)
# sns.scatterplot(x=k_values, y=res)
# plt.show()


y_pred = grid.predict(X_test)
print(classification_report(y_test,y_pred))
print(confusion_matrix(y_test, y_pred))