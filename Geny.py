import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, roc_auc_score, auc
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

df = pd.read_csv('gene_expression.csv')
# print(df.head())

# sns.scatterplot(data=df,x='Gene One',y='Gene Two',hue='Cancer Present')
# plt.show()

X = df.drop('Cancer Present', axis=1)
y = df['Cancer Present']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_trains = scaler.fit_transform(X_train)
X_tests = scaler.transform(X_test)

knn = KNeighborsClassifier()
knn.fit(X_trains, y_train)

test = pd.concat([pd.DataFrame(X_test), pd.DataFrame(y_test)], axis=1)

# sns.scatterplot(x='Gene One', y='Gene Two', hue='Cancer Present', data=test, alpha=0.7)
# plt.show()

y_pred = knn.predict(X_tests)

print(classification_report(y_test, y_pred))
# test_error_rates = []
# for k in range(1, 30):
#     knn_model = KNeighborsClassifier(n_neighbors=k)
#     knn_model.fit(X_trains, y_train)
#
#     y_pred_test = knn_model.predict(X_tests)
#
#     test_error = round((1 - accuracy_score(y_test, y_pred_test)),3)
#     test_error_rates.append(test_error)
#
# sns.lineplot(x=range(1,30),y=test_error_rates)
# plt.show()

# # print(knn.get_params().keys())
# operations = [('scaler',scaler),('knn',knn)]
# pipe = Pipeline(operations)
# k_values = list(range(1,20))
# param_grid = {'knn__n_neighbors': k_values}
# full_cv_classifier = GridSearchCV(pipe,param_grid,cv=5,scoring='accuracy')
# full_cv_classifier.fit(X_train,y_train)
# full_cv_classifier.best_estimator_.get_params()
# full_cv_classifier.cv_results_.keys()
# # print(len(k_values))
# full_cv_classifier.cv_results_['mean_test_score']
# # print(len(full_cv_classifier.cv_results_['mean_test_score']))
# knn14 = KNeighborsClassifier(n_neighbors=23)
# operations = [('scaler',scaler),('knn14',knn14)]
# pipe = Pipeline(operations)
# pipe.fit(X_train,y_train)
# pipe_pred = pipe.predict(X_test)
# print(classification_report(y_test,pipe_pred))
# single_sample=X_test.iloc[40]
# print(single_sample)
# print(pipe.predict(single_sample.values.reshape(1, -1)))
# print(pipe.predict_proba(single_sample.values.reshape(1, -1)))
