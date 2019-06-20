#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 16:25:04 2018

@author: r
"""

"""
Part A : Data Analysis
"""


# Importing relevant library functions.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


"""
Question 1 : Import the data from the url to a Pandas data frame.
"""

# Importing the data from the url to a Pandas data frame.
data=pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user", sep="|")


"""
Question 2 : Remove all entries with occupation other or retired from the data set. 
"""

# The function below changes occupation "other" and "retired" into None.
def change_occupation_to_none(occupation):
    if occupation == "other" or occupation == "retired":
        return None
    else:
        return occupation

# Applying the function to the data.
data.occupation = data.occupation.apply(change_occupation_to_none)

# Rejecting people whose occupation is None, which was "other" or "retired."
data.dropna(subset=["occupation"], inplace = True)


"""
Question 3 : Plot a bar chart.
"""

# The list below will contain data for the chart. [[occupation, number], ...]
list_for_chart = np.array([], dtype = object)

# The function below counts the number of people per occupation and puts the result into list_for_chart.
def func_for_chart(occupation):
    
    # Re-assigning list_for_chart.
    global list_for_chart
    
    if list_for_chart.shape == (0, ):
        # These lines are called when list_for_chart is empty.
        new_occupation = np.array([occupation, 1], dtype = object)
        list_for_chart = np.append(list_for_chart, new_occupation)
        list_for_chart = list_for_chart.reshape(1, 2)
        
    elif (occupation in list_for_chart[:, 0].tolist()):
        # These lines are called when list_for_chart already has line for "occupation."
        location = np.where(list_for_chart == occupation)[0][0]
        list_for_chart[location, 1] += 1
        
    else:
        # This line is called when list_for_chart doesn't have line for "occupation."
        new_occupation = np.array([occupation, 1], dtype = object)
        list_for_chart = np.append(list_for_chart, [new_occupation], axis=0)
        
    return occupation

# Applying the function.
data.occupation.apply(func_for_chart)

# Converting list_for_chart from np.ndarray into pd.Dataframe, in order to sort easily.
data_for_chart = pd.DataFrame(list_for_chart, columns=["occupation", "number"])

# Sorting data_for_chart.
data_for_chart = data_for_chart.sort_values("number", ascending=False)

# Converting list_for_chart from pd.Dataframe into np.ndarray
list_for_chart = data_for_chart.values

# The if statement below calculates number of people for "other."
# Checking whether the number of occupation in list_for_chart is greater than 10.
if list_for_chart.shape[0] > 10:
    
    for i in np.arange(10, list_for_chart.shape[0], 1):
        
        if i == 10:
            # This line is called first.
            # Changing the 11th greatest occupation, which will be showed on the chart as "other," into "other." 
            list_for_chart[i, 0] = "other"
            
        else:
            # Adding the 12th greatest occupation to the line for "other."
            list_for_chart[10, 1] += list_for_chart[11, 1]
            
            # Deleting the occupation which is already added to "other."
            # This makes the 13th greatest occupation 12th greatest.
            # Repeating this line allows us counting all of the number of people for "other."
            list_for_chart = np.delete(list_for_chart, 11, 0)

# Plotting the bar chart.
plt.bar(np.arange(list_for_chart.shape[0]), list_for_chart[:, 1])

# Labeling the occupations.
plt.xticks(np.arange(list_for_chart.shape[0]), list_for_chart[:, 0], rotation=45)

# Setting the title.
plt.title("the Number of People Per Occupation")

# Showing the chart.
plt.show()

"""
Question 4 : Find the mean and the standard deviaion of the age of people with the occupation: "administrator".
"""

# Exracting administrators and putting the data into administrator_data.
administrator_data = data[data["occupation"] == "administrator"]

# Printing the mean.
print("mean of administrators :", administrator_data["age"].mean())

# Printing the standard deviation.
print("standard deviation of administrators :", administrator_data["age"].std())
