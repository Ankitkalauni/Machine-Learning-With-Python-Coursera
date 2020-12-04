#libs
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

#data importing
df = pd.read_csv("FuelConsumptionCo2.csv")


#independed & dependent var
X = df.loc[:, ['ENGINESIZE']].values
y = df.loc[:, ['CO2EMISSIONS']].values

#data split in train and test
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.2, random_state = 44)

#Converting the X_train into Ploynomial Features with Degree 2
poly = PolynomialFeatures(degree = 2)
X_train_poly = poly.fit_transform(X_train)
print(X_train_poly)


#Linear regression model for polynomial regression on train set
from sklearn.linear_model import LinearRegression
regr = LinearRegression()
y_pred = regr.fit(X_train_poly, y_train)

print('Coefficient', regr.coef_ ,'\n', 'Intercept: ', regr.intercept_)

#ploting polynomial regression line through train dataset
plt.scatter(X_train, y_train,  color='blue')
XX = np.arange(0.0, 10.0, 0.1)
yy = regr.intercept_[0]+ regr.coef_[0][1]*XX+ regr.coef_[0][2]*np.power(XX, 2)
plt.plot(XX, yy, '-r' )
plt.title('Training Dataset')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()

#prediction on polynomial test dataset 
X_test_poly = poly.fit_transform(X_test)
y_test_ = regr.predict(X_test_poly)

#Evaluation
print("Mean absolute error: %.2f" % np.mean(np.absolute(y_test_ - y_test)))
print("Residual sum of squares (MSE): %.2f" % np.mean((y_test_ - y_test) ** 2))
print("R2-score: %.2f" % r2_score(y_test_ , y_test) )


#polynomial regression line through test dataset
plt.scatter(X_test, y_test,  color='blue')
XX = np.arange(0.0, 10.0, 0.1)
yy = regr.intercept_[0]+ regr.coef_[0][1]*XX+ regr.coef_[0][2]*np.power(XX, 2)
plt.plot(XX, yy, '-r' )
plt.title('Test Dataset')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()



#Converting the X_train into Ploynomial Features with Degree 3
poly = PolynomialFeatures(degree = 3)
X_test_poly = poly.fit_transform(X_test)
regr = regr.fit(X_test_poly, y_test)
y_test_ = regr.predict(X_test_poly)

print(regr.intercept_, regr.coef_)

plt.scatter(X_test, y_test, color = 'blue')
xx = np.arange(0.0, 8.0, 0.1)
yy = regr.intercept_[0] + regr.coef_[0][0]*xx + regr.coef_[0][1]*(xx)**1 + regr.coef_[0][2]*(xx)**2 + regr.coef_[0][3]*(xx)**3
plt.plot(xx,yy, color = 'r')
plt.title('Test Dataset')
plt.xlabel('Engine size')
plt.ylabel('Emission')
plt.show()

print('r2 score: %.2f' %r2_score(y_test_, y_test))
print('mse: %.2f' % np.mean((y_test_ - y_test)**2))
print('mae: %.2f' % np.mean((np.absolute(y_test_ - y_test))))