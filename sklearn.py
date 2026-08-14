from sklearn.tree import DecisionTreeClassifier
x = [[1],[2],[4],[5]]
y = ["fail","fail","pass","pass"]

model = DecisionTreeClassifier()
model.fit(x,y)

hours=[[3]]
prediction=model.predict(hours)
print(prediction)

from sklearn.svm import SVC
x = [[1],[2],[4],[5]]
y = ["fail","fail","pass","pass"]

model = SVC(kernel= "linear")
model.fit(x,y)

hours=[[3]]
prediction=model.predict(hours)
print(prediction)

from sklearn.neighbors import KNeighborsClassifier
x = [[1],[2],[3],[4],[5]]
y = ["fail","pass","fail","pass","pass"]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(x,y)

hours=[[2]]
prediction=model.predict(hours)
print(prediction)
