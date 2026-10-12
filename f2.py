import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# FIXED: We create the data directly in the script instead of loading an external file
data_dict = {
    "Study-Hours": [1.0, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0],
    "Result":      [0,   0,   0,   0,   1,   1,   1,   1,   1,   1]
}
data = pd.DataFrame(data_dict)

# Extract features and target
X = data[["Study-Hours"]]
y = data["Result"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Evaluate and Predict
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)

hours = pd.DataFrame({"Study-Hours": [3.5]})
prediction = model.predict(hours)

print("Prediction:", prediction[0])



import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

y_actual = [1, 1, 0, 0, 1]
y_probability = [0.90, 0.70, 0.40, 0.30, 0.80]

fpr, tpr, thresholds = roc_curve(y_actual, y_probability)

roc_auc = auc(fpr, tpr)

print("FPR:", fpr)
print("TPR:", tpr)
print("Thresholds:", thresholds)
print("AUC:", roc_auc)

plt.plot(fpr, tpr, marker="o")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.show()


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)

new_flower = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(new_flower)

print("Predicted class:", prediction[0])
print("Flower name:", iris.target_names[prediction[0]])