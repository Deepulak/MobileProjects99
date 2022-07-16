# in machine learning, while working with scikit learn library,
# we need to save the trained models in a file and 
# restore them in order to reuse it to compare 
# the model with othe models, to test the model on a 
# new data. The saving of data is called
# Serialization, while restoring the data is called
# Desrialization.
# we save and load machine learning
# with python pikle library

import numpy as np
from sklearn.datasets import load_iris

# load dataset
iris = load_iris()
X = iris.data
y = iris.data

# Split dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2018)

# import KNeigborsClassifier model
from sklearn.neigbors import KNeighborsClassifier as KNN
knn = KNN(n_neighbors=3)

# train modell
knn.fit(X_train, y_train)

# Save and Load Model Using Pickle
import pickle
# save to model to disk
filename = "final_model.csv"
pickle.dump(model, open(filename, "wb"))

# some time later ..

# load the model from the disk
load_model = pickle.load(open(filename, "rb"))
result = load_model.predict(X_test)
print(result)

# You can also use joblib class from 
# sklearn.externals, Joblib is the replacement os pickle as it is
# more efficent on objects that carry
# large numpy arrays. These fucntions also accepts
# file-like object instead of filenames



