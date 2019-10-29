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
fig.patch.set_facecolor('black')
ax = fig.add_subplot(111)
#frame=pd.DataFrame([6128,9879,5539,3609,3979,7426,3767,5210,6210,8642,3907,3175,6380,3985,3687,3723,8320,4975,3099,6330], index=[1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018])
#print(frame)
#plt.plot(frame[0])
#answer=[]
#xs=frame.index
#ys=frame.values
#m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /((mean(xs)*mean(xs)) - mean(xs*xs)))
    
#b = mean(ys) - m*mean(xs)
#m=-53
#b=113078
#plt.plot([1999,2018],[1999*m+b,2018*m+b],color='green')
plt.bar(10, 1,width=0.2,color='b',align='center')
plt.bar(10.2, 2,width=0.2,color='g',align='center')
plt.bar(10.4, 3,width=0.2,color='b',align='center')
plt.bar(10.6, 4,width=0.2,color='g',align='center')
plt.bar(10.8, 5,width=0.2,color='b',align='center')
plt.bar(11, 6,width=0.2,color='g',align='center')
plt.bar(11.2, 7,width=0.2,color='b',align='center')
plt.bar(11.2, 8,width=0.2,color='g',align='center')
plt.bar(11.4, 9,width=0.2,color='b',align='center')
plt.bar(11.6, 10,width=0.2,color='g',align='center')
plt.bar(11.8, 11,width=0.2,color='b',align='center')
plt.bar(12, 12,width=0.2,color='g',align='center')
plt.bar(12.2, 13,width=0.2,color='b',align='center')
plt.bar(12.4, 14,width=0.2,color='g',align='center')
plt.bar(12.6, 15,width=0.2,color='b',align='center')
plt.bar(12.8, 16,width=0.2,color='g',align='center')
plt.bar(13, 17,width=0.2,color='b',align='center')
plt.bar(13.2, 18,width=0.2,color='g',align='center')
plt.bar(13.4, 19,width=0.2,color='b',align='center')
plt.bar(13.6, 20,width=0.2,color='g',align='center')
plt.xticks([10,10.2,10.4,10.6,10.8,11,11.2,11.4,11.6,11.8,12,12.2,12.4,12.6,12.8,13,13.2,13.4,13.6,13.8],['11512307','11512304','11512302','11512286','11512268','11512231','11512198','11512190','11512141','11512126','11512119','11512114','11512112','11512088','11512082','11511992','11511990','11511964','11511961'],color='red')
plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],color='red')

plt.ylabel('rank',color='red')
plt.xlabel('the code of item')
plt.title('the frequency of top crimes in id 258138724',color='red')
ax.patch.set_facecolor('pink')
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
	
	# Yunhan's comment: Good job.
