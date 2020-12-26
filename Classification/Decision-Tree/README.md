## Decision Tree Classifier Python Intuition

### Pre-processing
Using my_data as the Drug.csv data read by pandas, declare the following variables:

	X as the Feature Matrix (data of my_data)
	y as the response vector (target)
Remove the column containing the target name since it doesn't contain numeric values.

As you may figure out, some features in this dataset are categorical such as Sex or BP. Unfortunately, Sklearn Decision Trees do not handle categorical variables. But still we can convert these features to numerical values. pandas.get_dummies() Convert categorical variable into dummy/indicator variables.

### Setting up the Decision Tree
We will be using train/test split on our decision tree. Let's import train_test_split from sklearn.cross_validation.

Now train_test_split will return 4 different parameters. We will name them:
X_trainset, X_testset, y_trainset, y_testset

The train_test_split will need the parameters:
X, y, test_size=0.3, and random_state=3.

The X and y are the arrays required before the split, the test_size represents the ratio of the testing dataset, and the random_state ensures that we obtain the same splits.

### Modeling
We will first create an instance of the DecisionTreeClassifier called drugTree.
Inside of the classifier, specify criterion="entropy" so we can see the information gain of each node.


Next, we will fit the data with the training feature matrix X_trainset and training response vector y_trainset


### Prediction
Let's make some predictions on the testing dataset and store it into a variable called predTree.


### Evaluation
Next, let's import metrics from sklearn and check the accuracy of our model.



### Accuracy classification score computes subset accuracy: the set of labels predicted for a sample must exactly match the corresponding set of labels in y_true.

In multilabel classification, the function returns the subset accuracy. If the entire set of predicted labels for a sample strictly match with the true set of labels, then the subset accuracy is 1.0; otherwise it is 0.0.


### Visualization

'''
# Notice: You might need to uncomment and install the pydotplus and graphviz libraries if you have not installed these before
#conda install -c conda-forge pydotplus -y
#conda install -c conda-forge python-graphviz -y
'''
