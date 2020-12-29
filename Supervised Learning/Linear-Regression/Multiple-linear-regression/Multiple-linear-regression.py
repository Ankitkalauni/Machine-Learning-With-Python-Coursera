#importing libs
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

#File Importing
df = pd.read_csv('FuelConsumptionCo2.csv')
df.columns
X = df.loc[:,['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY']].values
y = df.loc[:,['CO2EMISSIONS']].values

#Adding Columns of onces
ones = np.ones((len(X), 1), dtype= 'float')
X = np.concatenate((ones, X), axis = 1)
#X = X[:,1:]

#feature scalling
from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()
X = scalar.fit_transform(X)

#Spliting the data into train test
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8, random_state = 20)


#Multiple Linear regression
regr = LinearRegression()
regr.fit(X_train, y_train)
print ('Coefficients: ', regr.coef_)
print ('Intercept: ',regr.intercept_)

#Predicting
y_pred = regr.predict(X_test)

#Performance

print('\nPerformance:')
print("Residual sum of squares: %.2f" 
      % np.mean((y_pred - y_test) ** 2))
print('R2_Score: %2.3f' % r2_score(y_test, y_pred))
print('Variance score: %.2f' % regr.score(X_test, y_test))

