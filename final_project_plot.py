#Yaqin Wang
# Section E, Andrew Rickus
# 11/26/2018
# ISTA 131 HW7
# This assignment is for final project plot

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import csv
from collections import Counter
from scipy import stats
from numpy import array
from matplotlib import pylab


def get_data():
	filename = 'NBA_player_of_the_week.csv'
	df = pd.read_csv(filename)
	return df

def get_smaller_df(name):
	data= get_data()
	dic = Counter(data[name])
	index=[]
	data = []

	for key,value in sorted(dic.items()):
		index.append(key)
		data.append(value)
	result = pd.Series(data,index)
	new_df = pd.DataFrame(columns=['count'],index = result.index,data=result.values)
	
	
	return result

def make_fig1():
	df= get_smaller_df('Team')
	
	xAxis = df.index
	yAxis = df.values
	
	plt.bar(xAxis,yAxis)
	
	plt.title('Count Team',fontsize = 24)
	plt.xticks(fontsize=14,rotation = 40)
	plt.yticks(fontsize=24)
	plt.ylabel('Frequency',size = 24)
	plt.xlabel('Team Name',size = 24)
	
	plt.figure()
	


def make_fig2():
	df = get_data()
	weight = [int(ele) for ele in df['Weight'] if len(ele)==3]
	n, bins, patches = plt.hist(weight, 50, normed=1, facecolor='g', alpha=0.75)
	
	plt.grid(True)
	
	plt.xticks(fontsize=15)
	plt.yticks(fontsize=15)
	plt.ylabel('Probability',size = 24)
	plt.xlabel('Weight (Pounds)',size = 24)
	plt.title('Weight Distribution of NBA Player',fontsize = 24)
	plt.figure()

#Sourse from (regression line) https://plot.ly/matplotlib/linear-fits/
def make_fig3():
	df = get_data()
	x = [int(ele) for ele in df['Age'] ]

	y = [int(ele) for ele in df['Weight'] if len(ele)==3 ]

	#cover kg data to pounds
	for ele in df['Weight']:
		if(len(ele)!=3):
			kg_to_pound = int(ele[:ele.index('k')])*2.20462
			y.append(kg_to_pound)

	slope,intercept,r,p,str_err = stats.linregress(x,y)
	print('r = '+str(r))
	line = slope *array(x) + intercept
	plt.plot(x,y,'o',x,line)
	ax = plt.gca()
	fig = plt.gcf()
	
	plt.xticks(fontsize=15)
	plt.yticks(fontsize=15)
	plt.ylabel('Weight',size = 24)
	plt.xlabel('Age',size = 24)
	plt.title('Weight and Age Scatter Plot',size = 24)
	
def main():
	make_fig1()
	make_fig2()
	make_fig3()
	plt.show()
	

if __name__=="__main__":
	main()
	# Yunhan's comment: Good job.