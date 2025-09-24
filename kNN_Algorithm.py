"""
K-Nearest Neighbors (KNN) Algorithm Implementation
-------------------------------------------------
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from collections import Counter

X,y = make_classification (
    n_samples = 100,
    n_features = 2, #weight and height
    n_informative = 2, #imp features for classification
    n_redundant = 0,
    n_clusters_per_class = 2,
    random_state = 46
)
print(X.shape)
print(y.shape)

plt.Figure(figsize=(6,4))
plt.scatter(X[:,0],X[:,1],c=y,cmap = plt.cm.coolwarm , edgecolors = 'k')
plt.title("height vs weight")
plt.xlabel("weight")
plt.ylabel("height")
plt.show()

X_train , X_test, y_train, Y_test = train_test_split(X,y,test_size = 0.2 , random_state = 45)
#print(X_train)
print(X_test)


def euclidean(p1,p2):
  return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
def KNN(X_train,y_train,x,k): #tuple will be in x like (5,7)
  distances = [euclidean(x,i) for i in X_train]
  #distances = []
  #for i in X_train :
    #distance = euclidean(x,i)
    #distances.append(distance)
  k_nearest_neighbors_indices = np.argsort(distances)[:k]
  k_nearest_neighbors_classes = [y_train[i] for i in k_nearest_neighbors_indices]
  #classes = []
  #for i in k_nearest_neighbors_indices:
    #temp = y_train[i]
    #classes.append(temp)

  classes_count = Counter(k_nearest_neighbors_classes)
  output_class = classes_count.most_common(1)[0][0]
  return output_class
def predict_all(X_train, y_train, X_test, k):
  predictions = []
  for x in X_test:
    prediction = KNN(X_train, y_train, x,k)
    predictions.append(prediction)
  return predictions

predictions = predict_all(X_train,y_train,X_test,3)
print("predicitons: ",*predictions)
print("Actual : " ,*Y_test)

accuracy = np.mean(predictions == Y_test)
#for i in range (len(predictions)):
  #if predictions[i] == Y_test[i]:
    #count += 1
#accuracy = count / len(predictions)

print (f"accuracy:{accuracy*100:.2f}%")
