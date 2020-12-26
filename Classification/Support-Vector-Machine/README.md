## Support Vector Machine Classifier Python Intuition

### Data pre-processing and selection
Lets first look at columns data types:


### Train/Test dataset
Okay, we split our dataset into train and test se


### Modeling (SVM with Scikit-learn)

The SVM algorithm offers a choice of kernel functions for performing its processing. Basically, mapping data into a higher dimensional space is called kernelling. The mathematical function used for the transformation is known as the kernel function, and can be of different types, such as:

	1.Linear
	2.Polynomial
	3.Radial basis function (RBF)
	4.Sigmoid
	
Each of these functions has its characteristics, its pros and cons, and its equation, but as there's no easy way of knowing which function performs best with any given dataset, we usually choose different functions in turn and compare the results. Let's just use the default, RBF (Radial Basis Function) for this lab.

After being fitted, the model can then be used to predict new values:

### Evaluation
You can also easily use the f1_score from sklearn library:

### Practice
Can you rebuild the model, but this time with a __linear__ kernel? You can use __kernel='linear'__ option, when you define the svm. How the accuracy changes with the new kernel function?
