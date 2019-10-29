#Author:Yaqin Wang
#Date:2018/10/29
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean
import statistics
import json
from textblob import TextBlob
#this function will read a json file and filter the polarity and subjectivity are 0 and return a list of 
#the left numbers mean and standard deviation

fig = plt.figure()
#fig.patch.set_facecolor('black')
#ax = fig.add_subplot(111)
frame=pd.DataFrame([6128,9879,5539,3609,3979,7426,3767,5210,6210,8642,3907,3175,6380,3985,3687,3723,8320,4975,3099,6330], index=[1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018])
print(frame)
plt.plot(frame[0])
answer=[]
xs=frame.index
ys=frame.values
#m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /((mean(xs)*mean(xs)) - mean(xs*xs)))
    
#b = mean(ys) - m*mean(xs)
m=-53
b=113078
plt.plot([1999,2018],[1999*m+b,2018*m+b],color='green')
#plt.xticks([10,10.2,10.4,10.6,10.8,11,11.2,11.4,11.6,11.8,12,12.2,12.4,12.6,12.8,13,13.2,13.4,13.6,13.8],['2018-11-13T22:39:00','2018-11-13T18:09:00','2018-10-01T15:00:00','2017-06-30T12:00:00','2018-10-06T19:30:00','2018-10-21T00:00:00','2018-08-06T00:01:00','2018-11-03T14:45:00','2018-11-09T00:01:00','2018-11-12T19:10:00','2018-11-08T09:00:00','2018-09-27T08:30:00','2018-11-04T14:00:00','2018-11-12T12:10:00','2018-11-13T12:00:00','2018-11-13T09:00:00','2018-11-13T22:00:00','2018-11-13T17:00:00','2018-11-13T23:00:00'],color='red')
#plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],color='red')
plt.ylabel('the accident numbers',color='red')
plt.xlabel('year')
plt.title('the number of accident happened in different year',color='red')
#ax.patch.set_facecolor('pink')
	#plt.figure().patch.set_facecolor('red')
	#plt.facecolor('red')
	#plt.colors('red')
plt.show()


def get_ols_parameters(ser):
	answer=[]
	xs=ser.index
	ys=ser.values
	m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /((mean(xs)*mean(xs)) - mean(xs*xs)))
    
	b = mean(ys) - m*mean(xs)
	slope, intercept, r_value, p_value, std_err = stats.linregress(xs, ys)
	regression_line = [(m*x)+b for x in xs]
	result=coefficient_of_determination(ys,regression_line)
	answer.append(m)
	answer.append(b)
	answer.append(result)
	answer.append(p_value)
	return answer
def squared_error(ys_orig,ys_line):
    return sum((ys_line - ys_orig) * (ys_line - ys_orig))

def coefficient_of_determination(ys,regression_line):
    y_mean_line = [mean(ys) for y in ys]
    squared_error_regr = squared_error(ys, regression_line)
    squared_error_y_mean = squared_error(ys, y_mean_line)
    return 1 - (squared_error_regr/squared_error_y_mean)
    
	#m, b = best_fit_slope_and_intercept(xs,ys)
	

	#r_squared = coefficient_of_determination(ys,regression_line)
	#print(r_squared)
#this function will make the prediction of the given description
def main():
	print('0')
	get_sentiment('dataset.json')
	#frame=get_ct_sentiment_frame()
	#make_fig(frame)
