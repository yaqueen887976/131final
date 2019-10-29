'''
Name: Yaqin Wang
Section Leader: Andrew Rickus
Date: Nov 27th
ISTA 131 final project
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
import numpy as np


def prepare_data(data):
    '''
    Name: prepare_data
    Parameter: data -- a csv file
    Return value: a new data.
    '''
    new_data = pd.DataFrame()
    for column in data.columns:
        if data[column].isnull().sum() < 10:
            new_data[column] = data[column]

    new_data = new_data.dropna()
    return new_data

def third(new_data):
    '''
    Name: third
    Parameter: new_data
    Return value: None
    '''
    plt.hist(new_data['incom16'])
    plt.xlabel("Income")
    plt.ylabel("Frequecy of income")
    plt.title("Frequency vs Income")
    plt.show()

def main():
    data = pd.read_csv("gss_1972_to_2014_clean.csv")
    new_data = prepare_data(data)
    third(new_data)

main()