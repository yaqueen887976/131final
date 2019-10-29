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

def first(new_data):
    '''
    Name: first
    Parameter: new_data
    Return value: an image.
    '''
    new_data_year = pd.pivot_table(new_data, values='incom16', columns=['year'], aggfunc=np.mean).T
    new_data_year['incom16'].values


    year = [1972, 1973, 1974, 1975, 1976, 1977, 1978, 1980, 1982, 1983, 1984,
           1985, 1986, 1987, 1988, 1989, 1990, 1991, 1993, 1994, 1996, 1998,
           2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014]
    years_array = sm.add_constant(year)
    model = sm.OLS(new_data_year['incom16'], years_array)
    results = model.fit()
    print (results.params)

    plt.figure()
    ax = new_data_year['incom16'].plot(marker='')
    xs = np.arange(1972, 2014)
    ax.set_ylabel(r"RS FAMILY INCOME WHEN 16 YRS OLD") 
    ys = results.params['x1'] * xs + results.params['const']
    plt.plot(xs, ys, linewidth=1)
    plt.scatter(year, new_data_year['incom16'])
    plt.title("Income vs year")
    plt.show()

def main():
    data = pd.read_csv("gss_1972_to_2014_clean.csv")
    new_data = prepare_data(data)
    first(new_data)

main()