from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import tree
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.linear_model import LogisticRegression
import seaborn as sns
import pandas as pd
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/' #get rid of these when uploading to google collab and keep an eye out
import graphviz


df = pd.read_csv('data_classes.csv') #loading the dataset
df = df[df['Classified Income'].notna()]


features = df.drop('Classified Income', axis=1).values
target = df['Classified Income'].values

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=420)

classifier = LogisticRegression()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
result = pd.DataFrame({'Actual' : y_test, 'Predicted' : y_pred})
print(result)

cf_matrix = confusion_matrix(y_test, y_pred)
print(cf_matrix)

sns.heatmap(pd.DataFrame(cf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.show()

sns.histplot(df, x= 'Classified Income')
plt.show()
print('Accuracy of model')
print(accuracy_score(y_test,y_pred) * 100, '%')

target_names = ['0', '1', '2', '3', '4']
print('Classification report: \n', classification_report(y_test, y_pred,target_names=target_names))


clf = tree.DecisionTreeClassifier(max_depth=5)
clf = clf.fit(X_train, y_train)
text_representation = tree.export_text(clf)
print(text_representation)

