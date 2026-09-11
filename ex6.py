import numpy as np
from sklearn.tree import DecisionTreeClassifier
x = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
y = np.array(['Fail', 'Fail', 'Fail', 'Pass', 'Pass', 'Pass', 'Pass', 'Pass'])
model = DecisionTreeClassifier()
model.fit(x, y)
hours = [[2]]
prediction = model.predict(hours)
print(prediction)



import numpy as np
from sklearn.tree import DecisionTreeClassifier
x = np.array([[45], [50], [60], [70], [75], [80], [85], [90]])
y = np.array(['Not Eligible', 'Not Eligible', 'Not Eligible', 'Eligible', 'Eligible', 'Eligible', 'Eligible', 'Eligible'])
model = DecisionTreeClassifier()
model.fit(x, y)
attendance = [[55], [65], [72], [88]]
prediction = model.predict(attendance)
print(prediction)



import numpy as np
from sklearn.neighbors import KNeighborsClassifier
x = np.array([[18], [20], [22], [25], [30], [32], [35], [38]])
y = np.array(['Normal', 'Normal', 'Normal', 'Normal', 'Hot', 'Hot', 'Hot', 'Hot'])
model = KNeighborsClassifier(n_neighbors=3)
model.fit(x, y)
temperature = [[23], [28], [31], [36]]
prediction = model.predict(temperature)
print(prediction)



import numpy as np
from sklearn.svm import SVC
x = np.array([[15000], [20000], [25000], [30000], [35000], [40000], [50000], [60000]])
y = np.array(['Not Buy', 'Not Buy', 'Not Buy', 'Buy', 'Buy', 'Buy', 'Buy', 'Buy'])
model = SVC(kernel='linear')
model.fit(x, y)
salary = [[22000], [28000], [32000], [45000]]
prediction = model.predict(salary)
print(prediction)



import numpy as np
from sklearn.naive_bayes import GaussianNB
x = np.array([[25], [30], [35], [40], [45], [55], [65], [75]])
y = np.array(['Fail', 'Fail', 'Fail', 'Pass', 'Pass', 'Pass', 'Pass', 'Pass'])
model = GaussianNB()
model.fit(x, y)
marks = [[28], [37], [48], [70]]
prediction = model.predict(marks)
print(prediction)