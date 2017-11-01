#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    all = len(predictions)

    ### your code goes here
    for i in range(all):
        cleaned_data.append((ages[i][0], net_worths[i][0], abs(predictions[i][0] - net_worths[i][0])))

    print 'old', cleaned_data

    cleaned_data = sorted(cleaned_data, key=lambda item: item[2])

    for j in range(all / 10):
        cleaned_data.pop()

    print 'new', len(cleaned_data), cleaned_data

    return cleaned_data
