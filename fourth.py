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

def fourth(new_data):
    '''
    Name: fourth
    Parameter: new_data
    Return value: None
    '''
    new_data_year_mean = pd.pivot_table(new_data, values='hrs1', columns=['year'], aggfunc=np.mean).T
    new_data_year_mean = new_data_year_mean['hrs1'].values

    new_data_year_std = pd.pivot_table(new_data, values='hrs1', columns=['year'], aggfunc=np.std).T
    new_data_year_std = new_data_year_std['hrs1'].values
    year = [1972, 1973, 1974, 1975, 1976, 1977, 1978, 1980, 1982, 1983, 1984,\
       1985, 1986, 1987, 1988, 1989, 1990, 1991, 1993, 1994, 1996, 1998,\
       2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014]
    plt.errorbar(year, new_data_year_mean, yerr=new_data_year_std)
    plt.xlabel("Year")
    plt.ylabel("Mean working hour with Standard deviation")
    plt.show()

def main():
    data = pd.read_csv("gss_1972_to_2014_clean.csv")
    new_data = prepare_data(data)
    fourth(new_data)

main()