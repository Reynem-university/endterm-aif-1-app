# Chapter 9. The Clone Laboratory — Classical Machine Learning

## 9.1 ML Paradigms: Supervised vs. Unsupervised Learning

On the approach to Bowser's citadel, the villain deployed a legion of mechanical Toad copies and guard robots. To avoid wasting ammunition on allies, ROBO-LUMA had to instantly classify approaching objects by physical features (height, weight, body temperature, movement speed).

Luigi loaded two classical learning paradigms:

1. Supervised Learning: The model is trained on a labeled dataset {(x1,y1),…,(xn,yn)}, where vector xi contains object parameters, and yi∈{Friend,Enemy} is the exact class label.
2. Unsupervised Learning: Clustering unknown entities in feature space without prior labeling.

The dataset was split according to the classical standard: Train (60%) / Validation (20%) / Test (20%).

## 9.2 Decision Trees and Random Forest

For fast binary classification, the robot built a Decision Tree, choosing optimal split parameters by the criterion of Information Gain based on Shannon entropy:

```
H(S)=−pi∑pilog2(pi)
Gain(S,A)=H(S)−v∈Values(A)∑∣S∣∣Sv∣H(Sv)
```

To avoid overfitting, hundreds of trees were combined into a Random Forest ensemble using bagging:

```python
from sklearn.ensemble import RandomForestClassifier
# Features: [Height (cm), Weight (kg), Temperature (°C), Speed (m/s)]
X_train = [[30, 5, 36.6, 1.0], [120, 80, 60.0, 4.5], [35, 6, 36.5, 0.8], [110, 
75, 58.0, 5.0]]
y_train = [0, 1, 0, 1] # 0: Toad (Friend), 1: Mecha-Koopa (Enemy)
clf = RandomForestClassifier(n_estimators=100, max_depth=5)
clf.fit(X_train, y_train)
# New unrecognized entity on scanner
new_entity = [[115, 78, 59.0, 4.8]]
prediction = clf.predict(new_entity)
print("Recognition result:", "ENEMY!" if prediction[0] == 1 else "FRIEND")
```

![Место для изображения: дерево решений и случайный лес](assets/chapter9.jpg)

## 9.3 K-Means Clustering

To analyze unknown anomalous objects at long-range approaches, the robot activated the K-Means algorithm, iteratively minimizing the sum of squared distances from objects to cluster centroids:

```
J=j=1∑ki∈Cj∑∣∣xi−μj∣∣2
```

This allowed the robot to clear the perimeter of enemy spies in a fraction of a second.
