'''
    Author : Yaqin Wang
    Due: 11/26/2018
    ISTA 131, Final Project
'''
import pandas as pd, numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def get_data():
    df = pd.read_csv("dataset.csv", index_col=0)
    data = pd.DataFrame(index=df.index, columns=["cares", "support", "romantic", "alone", "needromance", "degree"])
    data["cares"] = df["cares"]
    data["support"] = df["support"]
    data["romantic"] = df["romantic"]
    data["alone"] = df["alone"]
    data["needromance"] = df["needromance"]
    data["degree"] = df["degree"]
    return data.dropna()

def add_loneliness(data):
    data["rev_cares"] = 6 - data["cares"]
    data["rev_support"] = 6 - data["support"]
    data["rev_romantic"] = 6 - data["romantic"]
    data["emotional_loneliness"] = (data["rev_cares"] + data["rev_romantic"] + data["rev_support"] + data["alone"] + data["needromance"])/5

def get_x_and_y(data):
    median = data["degree"].median()
    sorted_by_degree = data.sort_values(by=["degree"])
    #print(sorted_by_degree)
    smaller = sorted_by_degree.loc[data['degree'] < median]
    greater = sorted_by_degree.loc[data['degree'] >= median]
    statistic, p_value = stats.ttest_ind(smaller["emotional_loneliness"].values, greater["emotional_loneliness"].values)
    x = ["Degree < "+str(median), "Degree >= " + str(median)]
    y = [smaller["emotional_loneliness"].mean(), greater["emotional_loneliness"].mean()]
    return x,y,p_value

def make_fig(x, y, p_value):
    plt.plot([0,1], y)
    plt.suptitle("Emotional Loneliness vs. \nDegree(How many contacts people have)",fontsize=28)
    plt.ylabel("Emotional Loneliness (1 to 5)", fontsize=24)
    plt.xlabel("Degree", fontsize=24)
    plt.tick_params(axis='x', labelsize=25)
    plt.tick_params(axis='y', labelsize=22)
    text = "P-value = " + str(round(p_value, 3)) + "(Two-tail T-test)"
    #print(text)
    plt.text(0.5, 2.06, text, fontsize=20)
    plt.xticks([0,1], x)
    #plt.text(2.97, 3.31, text, fontsize=10)
    
def main():
    data = get_data()
    #print(len(data.index))
    add_loneliness(data)
    x,y,p_value = get_x_and_y(data)
    
    plt.figure(figsize=(13,9))
    make_fig(x, y, p_value)
    plt.show()
    
if __name__ == "__main__":
    main()
    # Yunhan's comment: Good job.