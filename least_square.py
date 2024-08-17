import numpy as np
import matplotlib.pyplot as plt

# Preprocessing Input data
X = np.array(eval(input()))
Y = np.array(eval(input()))

# Mean
X_mean =np.mean(X)
Y_mean =np.mean(Y) 

num=0 #for slope
denom=0 #for slope

#to find sum of (xi-x') & (yi-y') & (xi-x)^2 
for i in range(len(X)): 
    num+=(X[i]-X_mean)*(Y[i]-Y_mean) 
    denom+= (X[i]-X_mean)**2

#calculate slope 
m=num/denom

#calculate intercept 
b=Y_mean-m*X_mean

print(m,b) 

#Line equation 
y_predicted=m*X+b 
print(y_predicted)

#to plot graph
plt.scatter(X,Y)
plt.plot(X,y_predicted,color='red')
plt.show()