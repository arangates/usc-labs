#import data from data.csv that contains Year and Rate as inputs 
import csv
import random
import numpy as np
import matplotlib.pyplot as pl

#converting the csv file into a list of tuples
with open('data.csv') as input_file:
	next(input_file,None) #ignoring the first tuple ('Year','Rate') from the list
	reader = [tuple(line) for line in csv.reader(input_file)]
	data = [tuple(filter(None, tp)) for tp in reader] #removing any white spaces left inside each tuple collection
print "data: ",data #data is a list of tuples of the form (x,y)

#making a seperate list for x and y
#x is a list containing Years
#y is a list containing Rates
x,y=map(list,zip(*data))

print "x list: ", x
print "y list: ", y

#calculating number of cases to be considered for training
print "total datasets: ",len(data)
rand_len=(len(data))/5
print "total training datasets: ",rand_len

#generating a list i containing the training cases
for i in range(rand_len):
	i= random.sample(data,rand_len)
i.sort()

train_x,train_y = map(list,zip(*i))
train_x = list(map(float, train_x));
train_y = list(map(float, train_y));

print "training list x: ",train_x
print "training list y: ",train_y

#use pylab to plot x and y
pl.plot(train_x,train_y)

#give plot a title
pl.title('Plot of y vs x')

#make axis labels
pl.xlabel('x axis')
pl.ylabel('y axis')

#set axis limits
#pl.xlim(1950, 2050.0)
#pl.ylim(0.0, 30.0)

#show plot on the screen
pl.show()

