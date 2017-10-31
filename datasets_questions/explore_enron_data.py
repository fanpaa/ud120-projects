#!/usr/bin/python
# -*- coding: utf-8 -*-

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print enron_data["SKILLING JEFFREY K"]

# s = 0
# e = 0
# for x in enron_data:
#     s = s + 1
#     if enron_data[x]["total_payments"] == 'NaN':
#         e = e + 1
#
# print 'total_payments', e,'all',s

count = 0
all = 0
p = 0
for x in enron_data:
    all = all + 1
    if enron_data[x]['poi'] == True:  # and enron_data[x]["total_payments"] == 'NaN':
        count = count + 1

    if enron_data[x]["total_payments"] == 'NaN':
        p = p + 1
print count, all,p
