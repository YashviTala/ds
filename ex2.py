import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# 1. FIXED: Added 'r' for raw string and pointing to a dataset file instead of the .py file
data = pd.read_csv(r"C:\Users\KC\Desktop\your_actual_dataset.csv") 

# 2. Extract features and target
X = data[["Study-Hours"]]
y = data["Result"]

# 3. Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 4. Train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 5. Evaluate and Predict
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)

hours = pd.DataFrame({"Study-Hours": [3.5]})
prediction = model.predict(hours)
print("Prediction:", prediction[0])
