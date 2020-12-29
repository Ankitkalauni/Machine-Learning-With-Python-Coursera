#libs
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#importing dataset
df = pd.read_csv(r'FuelConsumptionCo2.csv')

df.columns

X = df.loc[:,['ENGINESIZE']].values
y = df.loc[:,['CO2EMISSIONS']].values

#Spliting dataframe
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 43)


#Modeling
#Using sklearn package to model data
from sklearn import linear_model
regr = linear_model.LinearRegression()
regr.fit (X_train, y_train)
# The coefficient and intercept
print ('Coefficients: ', regr.coef_)
print ('Intercept: ',regr.intercept_)



#ploting Simple Linear Regression line on training dataset
plt.scatter(X_train, y_train,  color='blue')
plt.title('Train Set')
plt.plot(X_train, regr.coef_[0][0]*X_train + regr.intercept_[0], '-r')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()

#prediction
y_pred = regr.predict(X_test) #compare the y_pred and y_test
result = np.concatenate((y_test, y_pred), axis = 1)

#ploting Simple Linear Regression line on test dataset
plt.scatter(X_test, y_test, color = 'blue')
plt.title('Test Set')
plt.plot(X_test, regr.coef_[0][0]*X_test + regr.intercept_[0], '-r')
plt.xlabel('Engine Size')
plt.ylabel("Emission")
plt.show()

#acurate testing
from sklearn.metrics import r2_score
print("Mean absolute error: %.2f" % np.mean(np.absolute(y_pred - y_test)))
print("Residual sum of squares (MSE): %.2f" % np.mean((y_pred - y_test) ** 2))
print("R2-score: %.2f" % r2_score(y_test , y_pred) )

