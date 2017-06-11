import pylab as pl
import numpy as np
from sklearn import linear_model

#Load data
BSA=[[50,1.22],[25,0.958],[12.5,0.792],[6.25,0.758]]
BSA=np.array(BSA)

#Create linear regression object
regr=linear_model.LinearRegression()

#Define X and Y, use only one feature
X=BSA[:,[0]]
Y=BSA[:,[1]]

#Fit
regr.fit(X,Y)

#Plotting
pl.scatter(X,Y,color='black')
pl.plot(X,regr.predict(X),color='red',linewidth=1)

#Fomula
k=regr.coef_
b=regr.intercept_
R_square=1-np.mean((regr.predict(X)-Y)**2)

pl.title("y=%.4lf x + %.4lf \n R^2=%.4lf" %(k,b,R_square))

pl.show()