#to train and test  datasets using linear regression
#datasets are imported as csv files
import csv
import random
import numpy as np
import matplotlib.pyplot as pl
 
#converting the csv file into list of tuples
with open('ex1data1.csv') as input_file:
        next(input_file,None) #ignoring the first tuple ('Year','Rate') from th$
        reader = [tuple(line) for line in csv.reader(input_file)]
        data = [tuple(filter(None, tp)) for tp in reader] #removing any white s$
print "data: ",data #data is a list of tuples of the form (x,y)

x, y= map(list,zip(*data)) #x and y values made into seperate lists

x = list(map(float, x))
y = list(map(float, y))
print "x list: ",x
print "y list: ",y

#calculating total datasets given
def total_traindata(data, split):
	print "total datasets: ",len(data)
	n = len(data)*split
	print "total training datasets: ",n, int(n)
	return int(n)

#generating a list i containing the training cases
def collecting_traindata(data, n):
	for i in range(n):
		i = random.sample(data, n)
	i.sort()

	#splitting x and y into seperate lists
	train_x,train_y = map(list,zip(*i))
	train_x = list(map(float, train_x))
	train_y = list(map(float, train_y))

	print "training list x: ",train_x
	print "training list y: ",train_y

	return (train_x, train_y)

#calculating the predicted_y value (y=mx+c)
def calculating_pred_y(data, n):
	train_x, train_y = collecting_traindata(data, n)
	sum_x = 0
	sum_y = 0
	sum_xy = 0
	sum_xx = 0
	for i in range(n):
		sum_x += train_x[i]
		sum_y += train_y[i]
		sum_xy += (train_x[i] * train_y[i])
		sum_xx += (train_x[i])**2
	m = ((n * sum_xy)-(sum_x * sum_y))/((n * sum_xx)-(sum_x**2))
	b = (sum_y - (m * sum_x))/n
	pred_x = sum_x/n
	pred_y = (m * pred_x) + b
	return (pred_x,pred_y)

#calculating SSE
def sse(predicted_y, y):
	sum_of_sq_errors = 0.0 #sse is initialised to zero
	for i in range(len(y)):
		sum_of_sq_errors += (predicted_y - y[i])**2
	return sum_of_sq_errors

count = 0
sq_error_list=[]
final_y = 0
sum_of_sq_error = 0
#training data = 20%, test data = 80% => split=0.2
split = 0.2
n=total_traindata(data, split)
for count in range(10):
	predicted_x,predicted_y = calculating_pred_y(data, n) 
	sum_of_sq_error = sse(predicted_y, y)
	sq_error_list.append(sum_of_sq_error)
	if(sum_of_sq_error == min(sq_error_list)):
		final_x = predicted_x
		final_y = predicted_y
print "sse list: ", sq_error_list
print "minimum sq_error: ", min(sq_error_list)
print "final_y: ", final_y

#plot the results
pl.plot(x,y,'ro')
#pl.plot(np.unique(final_x), np.poly1d(np.polyfit(final_x,final_y,1))(np.unique(final_x)))
pl.title('Linear regression')
pl.xlabel('x axis')
pl.ylabel('y axis')
pl.show()




