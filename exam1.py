from sklearn.tree import DecisionTreeClassifier

X = [[1], [2], [4], [5]]
y = ["Fail", "Fail", "Pass", "Pass"]

model = DecisionTreeClassifier()
model.fit(X, y)

hours = [[3]]
prediction = model.predict(hours)

print(prediction)



from sklearn.naive_bayes import GaussianNB

X = [[1], [2], [4], [5]]
y = ["Fail", "Fail", "Pass", "Pass"]

model = GaussianNB()
model.fit(X, y)

hours = [[3]]
prediction = model.predict(hours)

print(prediction)


from sklearn.svm import SVC

X = [[1], [2], [4], [5]]
y = ["Fail", "Fail", "Pass", "Pass"]

model = SVC(kernel="linear")
model.fit(X, y)

hours = [[3]]
prediction = model.predict(hours)

print(prediction)



from sklearn.neighbors import KNeighborsClassifier

X = [[1], [2], [4], [5]]
y = ["Fail", "Fail", "Pass", "Pass"]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

hours = [[3]]
prediction = model.predict(hours)

print(prediction)

from sklearn.neural_network import MLPClassifier

x = [[1], [2], [4], [5]]
y = ["Fail", "Fail", "Pass", "Pass"]

model = MLPClassifier(hidden_layer_sizes=(2,), max_iter=5000, random_state=42)
model.fit(x, y)

hours = [[6]]
prediction = model.predict(hours)
print(prediction)
