#libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import preprocessing

#preprocessing
#reading csv file
df = pd.read_csv('teleCust1000t.csv')
df.head()

#Data Visualization and Analysis

#Let’s see how many of each class is in our data set
df['custcat'].value_counts()

df.hist(column='income', bins=50)

#spliting data into features & labels
X = df[['region', 'tenure','age', 'marital', 'address', \
        'income', 'ed', 'employ','retire', 'gender', 'reside']].values.astype(float)
y = df['custcat'].values

#Standarization
X = preprocessing.StandardScaler().fit(X).transform(X)

#spliting data into train test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=4)
print ('Train set:', X_train.shape,  y_train.shape)
print ('Test set:', X_test.shape,  y_test.shape)


#Classification
#K nearest neighbor (KNN)
from sklearn.neighbors import KNeighborsClassifier

# =============================================================================
# k=4
# =============================================================================

k = 6 #4
#Train Model and Predict  
neigh = KNeighborsClassifier(n_neighbors = k).fit(X_train,y_train)
neigh

#prediction
yhat = neigh.predict(X_test)
yhat = yhat.reshape(-1,1)
y_test = y_test.reshape(-1,1)
result = np.concatenate((y_test, yhat), axis = 1)

#Accuracy evaluation
'''
In multilabel classification, accuracy classification score is a
function that computes subset accuracy. This function is equal to
the jaccard_similarity_score function. Essentially, it calculates
how closely the actual labels and predicted labels are matched in 
the test set.
'''

from sklearn import metrics
print("Train set Accuracy: %.4f" %metrics.accuracy_score(y_train,neigh.predict(X_train)))
print("Test set Accuracy: %.4f" %metrics.accuracy_score(y_test, yhat))


# =============================================================================
# change k=6 and run the code again and check the accuracy
#
# when k=4
# Train set Accuracy:  0.5475
# Test set Accuracy:  0.32
# 
# #when k=6
# Train set Accuracy:  0.51625
# Test set Accuracy:  0.31
# =============================================================================

#for selection the vlaue of k and check the accuracy
Ks = 10
mean_acc = np.zeros((Ks-1))
std_acc = np.zeros((Ks-1))

for n in range(1,Ks):
    
    #Train Model and Predict  
    neigh = KNeighborsClassifier(n_neighbors = n).fit(X_train,y_train)
    yhat=neigh.predict(X_test)
    mean_acc[n-1] = metrics.accuracy_score(y_test, yhat)

    
    std_acc[n-1]=np.std(yhat==y_test)/np.sqrt(yhat.shape[0])

mean_acc


#ploting accuracy
plt.plot(range(1,Ks),mean_acc,'g')
plt.title('K\'s Accuracy')
plt.fill_between(range(1,Ks),mean_acc - 1 * std_acc,mean_acc + 1 * std_acc, alpha=0.10)
plt.fill_between(range(1,Ks),mean_acc - 3 * std_acc,mean_acc + 3 * std_acc, alpha=0.10,color="green")
plt.legend(('Accuracy ', '+/- 1xstd','+/- 3xstd'))
plt.ylabel('Accuracy ')
plt.xlabel('Number of Neighbors (K)')
plt.tight_layout()
plt.show()


print( "The best accuracy was with", mean_acc.max(), "with k=", mean_acc.argmax()+1) 
