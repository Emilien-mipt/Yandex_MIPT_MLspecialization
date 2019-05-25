import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics 

class KNN:
    def eucl_dist(self, X1, X2):
        dist = 0
        for i in range(X1.shape[0]):
            dist += (X1[i] - X2[i])**2
        return dist

    def label(self, X_train, point):
        arr_dist = [self.eucl_dist(x, point) for x in X_train]
        return y_train[arr_dist.index(min(arr_dist))]

    def predict(self, X_train, X_test):
        res = [self.label(X_train, x) for x in X_test]
        return np.array(res)


# Load and split the data
digits = datasets.load_digits()
X = digits.data
y = digits.target

(X_train, 
 X_test, 
 y_train, y_test) = train_test_split(X, y, test_size=0.25, shuffle = False, random_state = 0)

knn = KNN()
prediction = knn.predict(X_train, X_test)

accuracy = metrics.accuracy_score(y_test, prediction)
print(accuracy)
