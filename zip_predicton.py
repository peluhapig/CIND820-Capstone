from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import tree
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.linear_model import LogisticRegression
import seaborn as sns
import pandas as pd
from sklearn.ensemble import RandomForestClassifier 
import random
import pprint
from timeit import default_timer as timer


rands = random.sample(range(1, 100000), 20) #creates 20 random seeds fpr us to use

cf_lr = np.empty((5, 5))  #empty array to add cf of log reg
cf_dt = np.empty((5, 5)) #empty array to add cf of decision tree
cf_rf = np.empty((5, 5)) #empty array to add cf of random forest

time_lr = 0 #time for log reg
time_dt = 0 #time for decision tree
time_rf = 0 #time for random forest

df = pd.read_csv('data_classes.csv') #loading the dataset
df = df[df['Classified Income'].notna()] #get rid of empty entries


features = df.drop('Classified Income', axis=1).values 
target = df['Classified Income'].values

for rs in rands:

    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=rs) #initiate 80/20 split

    start = timer()

    log = LogisticRegression(solver='liblinear') #using liblinear as our dataset is on the smaller side
    log.fit(X_train, y_train)
    y_pred = log.predict(X_test) #predict values using log reg
    
    end = timer()

    time_lr += (end - start)

    result = pd.DataFrame({'Actual' : y_test, 'Predicted' : y_pred})
    
    cf_matrix_lr = confusion_matrix(y_test, y_pred)
    cf_lr += cf_matrix_lr
    # sns.heatmap(pd.DataFrame(cf_matrix_lr), annot=True, cmap="YlGnBu" ,fmt='g')
    # plt.title('Confusion matrix', y=1.1)
    # plt.ylabel('Actual label')
    # plt.xlabel('Predicted label')
    # plt.show()

    # sns.histplot(df, x= 'Classified Income')
    # plt.show()
    # print('Accuracy of model')
    # print(accuracy_score(y_test,y_pred) * 100, '%')

    target_names = ['0', '1', '2', '3', '4']
    class_rep_lg = classification_report(y_test, y_pred,target_names=target_names)
    start = timer()

    clf = tree.DecisionTreeClassifier(max_depth=4)
    clf = clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test) #predict values using decision tree
    end = timer()

    time_dt += (end - start)

    text_representation = tree.export_text(clf, feature_names= df.drop('Classified Income', axis=1).keys()) #makes sure the names are of the columns
    #print(text_representation)
    cf_matrix_dt = confusion_matrix(y_test, y_pred)
    cf_dt += cf_matrix_dt

    target_names = ['0', '1', '2', '3', '4']
    class_rep_dt = classification_report(y_test, y_pred,target_names=target_names)

    start = timer()
    rf = RandomForestClassifier(n_estimators=50, max_depth=7, n_jobs=-1, random_state= rs) #trains random forest with the optimized number of n_estimators
    rf.fit(X_train, y_train) 
    y_pred = rf.predict(X_test) 
    end = timer()

    time_rf += (end - start)

    cf_matrix_rf = confusion_matrix(y_test, y_pred)
    
    cf_rf += cf_matrix_rf

    target_names = ['0', '1', '2', '3', '4']
    class_rep_rf = classification_report(y_test, y_pred,target_names=target_names)

# sns.heatmap(pd.DataFrame(cf_lr), annot=True, cmap="YlGnBu" ,fmt='g')
# plt.title('Confusion matrix', y=1.1)
# plt.ylabel('Actual label')
# plt.xlabel('Predicted label')
# plt.show()


# sns.heatmap(pd.DataFrame(cf_dt), annot=True, cmap="YlGnBu" ,fmt='g')
# plt.title('Confusion matrix', y=1.1)
# plt.ylabel('Actual label')
# plt.xlabel('Predicted label')
# plt.show()

# sns.heatmap(pd.DataFrame(cf_rf), annot=True, cmap="YlGnBu" ,fmt='g')
# plt.title('Confusion matrix', y=1.1)
# plt.ylabel('Actual label')
# plt.xlabel('Predicted label')
# plt.show()

#The above code prints out the confusion matricies when uncommented

#Test Statistics
def test_stats(cm):
    TP = np.diag(cm) #contains a list of the TP values for our classes
    FP = np.sum(cm, axis=1) - TP #same length array as the above, selectign the column and summing
    FN = np.sum(cm, axis=0) - TP #Similar as above except selecting row 
    num_classes = 5
    TN = []
    for i in range(num_classes):
        temp = np.delete(cm, i, 0)    # delete ith row
        temp = np.delete(temp, i, 1)  # delete ith column
        TN.append(sum(sum(temp))) #two sums are applied to signal that we are summing the entire temp matrix, it's a 4x4
    accuracy = (TP+TN)/(TP+FP+FN+TN)
    precision = TP/(TP+FP) 
    recall = TP/(TP+FN)
    f_score = (2*precision*recall)/(precision+recall)
    output = {}
    for i in range(num_classes):
        output[i] = {"Accuracy": round(accuracy[i],2), "Percision": round(precision[i],2), "Recall": round(recall[i],2), "f-score": round(f_score[i],2)} 

    df_output = pd.DataFrame.from_dict(output) #honestly this is just for it to look nice, i may not have seen the sun in days but my outputs should be pretty 
    return(df_output) 

print("Log Reg Test Stats")
pprint.pprint(test_stats(cf_lr))

print("Disision Tree Test Stats")
pprint.pprint(test_stats(cf_dt))

print("Random Forest Test Stats")
pprint.pprint(test_stats(cf_rf))

# print(text_representation)
# plt.figure(figsize=(24,24))
# tree.plot_tree(clf,feature_names= df.drop('Classified Income', axis=1).keys())
# plt.show()

# print("Average Time Logistic Regression: " + str(time_lr/20))
# print("Average Time Decision Tree: " + str(time_dt/20))
# print("Average Time Random Forest: " + str(time_rf/20))