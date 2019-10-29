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
    data = pd.DataFrame(index=df.index, columns=["cares", "support", "romantic", "alone", "needromance", "trust"])
    data["cares"] = df["cares"]
    data["support"] = df["support"]
    data["romantic"] = df["romantic"]
    data["alone"] = df["alone"]
    data["needromance"] = df["needromance"]
    data["trust"] = df["trust"]
    return data.dropna()

def add_loneliness(data):
    data["rev_cares"] = 6 - data["cares"]
    data["rev_support"] = 6 - data["support"]
    data["rev_romantic"] = 6 - data["romantic"]
    data["emotional_loneliness"] = (data["rev_cares"] + data["rev_romantic"] + data["rev_support"] + data["alone"] + data["needromance"])/5

def convert_to_frequency(data):
    x = []
    for row in data.index:
        if data.loc[row]["emotional_loneliness"] not in x:
            x.append(data.loc[row]['emotional_loneliness'])
    ts = pd.Series(index=x)
    ts = ts.sort_index()
    # print(data["trust"][data["emotional_loneliness"] == 1.0].mean())
    
    for label in ts.index:
        ts[label] = round(data["trust"][data["emotional_loneliness"] == label].mean(), 2)
    return ts
def make_fig(x, y):
    plt.scatter(x, y, alpha=0.5)
    plt.suptitle("Emotional Loneliness vs. \nTrust(How much trust on others)",fontsize=28)
    plt.xlabel("Emotional Loneliness (1 to 5)", fontsize=24)
    plt.ylabel("Trust (1 to 5)", fontsize=24)

    plt.tick_params(axis='x', labelsize=25)
    plt.tick_params(axis='y', labelsize=22)
    
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x,p(x),"r--")
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    regression = "y = " + str(round(slope, 2)) +" * x + " + str(round(intercept,2))
    plt.text(2.97, 3.31, "R-squred = " + str(round(r_value ** 2, 3)), fontsize=20)    
    plt.text(1.8, 3.25, regression, fontsize=20)    
def main():
    data = get_data()
    add_loneliness(data)
    ts = convert_to_frequency(data)
    
    plt.figure(figsize=(13,9))
    make_fig(ts.index.values, ts.values)
    plt.show()
    
if __name__ == "__main__":
    main()