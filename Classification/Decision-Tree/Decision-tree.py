#libs
import numpy as np 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from matplotlib import pyplot as plt

#reading csv file
df = pd.read_csv(r'drug200.csv')

#preprocessing
X = df[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']].values
y = df.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder
label = LabelEncoder()

#for sex feature [male and female]
X[:,1] = label.fit_transform(X[:,1])

#for bp
X[:,2] = label.fit_transform(X[:,2])

#for cholesterol
X[:,3] = label.fit_transform(X[:,3])

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 3)

print(X_train.shape, y_train.shape)


dtree = DecisionTreeClassifier(criterion = 'entropy', max_depth = 4)
dtree.fit(X_train, y_train)

dtree_pred = dtree.predict(X_test)  #predicton

#Evaluation
from sklearn import metrics
print("DecisionTrees's Accuracy: ", metrics.accuracy_score(y_test, dtree_pred))


from  io import StringIO
import pydotplus
import matplotlib.image as mpimg
from sklearn import tree


dot_data = StringIO()
filename = "drugtree.png"
featureNames = df.columns[0:5]
targetNames = df["Drug"].unique().tolist()
out=tree.export_graphviz(dtree,feature_names=featureNames, out_file=dot_data, class_names= np.unique(y_train), filled=True,  special_characters=True,rotate=False)  
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png(filename)
img = mpimg.imread(filename)
plt.figure(figsize=(100, 200))
plt.imshow(img,interpolation='nearest')


