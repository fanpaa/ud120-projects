#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

### your code goes here


from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import precision_score,recall_score

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
pred = clf.predict(X_test)
print 'pred', pred

acc = clf.score(X_test, y_test)
precision_score(y_test, pred)

print 'X_test', len(X_test), X_test
print 'y_test', len(y_test), y_test
print 'acc', acc
print 'precision_score', precision_score(y_test, pred)
print 'recall_score', recall_score(y_test, pred)
