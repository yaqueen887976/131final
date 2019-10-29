'''
    Author : Yaqin Wang
    Due: 10/11/2018
    ISTA 131, Proj06
'''
import pandas as pd, numpy as np
import matplotlib.pyplot as plt



def main():
    names = ['group_a', 'group_b', 'group_c']
    values = [1, 10, 100]

    plt.figure(1, figsize=(9, 3))

    plt.subplot(131)
    plt.bar(names, values)
    plt.subplot(132)
    plt.scatter(names, values)
    plt.subplot(133)
    plt.plot(names, values)
    plt.suptitle('Categorical Plotting')
    plt.show()

if __name__ == "__main__":
    main()