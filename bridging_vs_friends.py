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
    data = pd.DataFrame(index=df.index, columns=["connected", "spendtime", "newthings", "community", "newpeople", "friends"])
    data["connected"] = df["connected"]
    data["spendtime"] = df["spendtime"]
    data["newthings"] = df["newthings"]
    data["community"] = df["community"]
    data["newpeople"] = df["newpeople"]
    data["friends"] = df["friends"]
    return data.dropna()

def add_bridging(data):
    data["bridging"] = (data["connected"] + data["spendtime"] + data["newthings"] + data["community"] + data["newpeople"])/5

def get_ts(data):
    ts = pd.Series(index=[1, 2, 3, 4, 5])
    ts[1] = data['bridging'][data['friends'] == 1].mean()
    ts[2] = data['bridging'][data['friends'] == 2].mean()
    ts[3] = data['bridging'][data['friends'] == 3].mean()
    ts[4] = data['bridging'][data['friends'] == 4].mean()
    ts[5] = data['bridging'][data['friends'] == 5].mean()
    return ts

def make_fig(x, y):
    x_axis = ["<100", "101-200", "201-300", "301-400", ">400"]
    plt.bar(x, y, alpha=0.5, color=["rosybrown", "lightcoral", "indianred", "brown", "firebrick"])
    plt.suptitle("Bridging Social Capital vs. Friends",fontsize=28)
    plt.xlabel("Friends", fontsize=24)
    plt.ylabel("Bridging Social Capital", fontsize=24)

    plt.tick_params(axis='x', labelsize=22)
    plt.tick_params(axis='y', labelsize=22)
    
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x,p(x),"r--")
    for i in range(len(x)):
        plt.text(x = x[i] - 0.22 , y = y[i]+0.01, s = "n = " + str(round(y[i], 2)), size = 15)

    '''
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    regression = "y = " + str(round(slope, 2)) +" * x + " + str(round(intercept,2))
    plt.text(2.97, 3.31, "R-squred = " + str(round(r_value ** 2, 3)), fontsize=20)    
    plt.text(1.8, 3.25, regression, fontsize=20)  
    '''
    plt.xticks([1, 2, 3, 4, 5], x_axis)  

def main():
    data = get_data()
    add_bridging(data)    
    ts = get_ts(data)
    plt.figure(figsize=(13,9))
    make_fig(ts.index.values, ts.values)
    plt.show()
    
if __name__ == "__main__":
    main()