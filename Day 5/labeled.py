from sklearn.tree import DecisionTreeClassifier

x = [
    [90, 5],
    [80, 4],
    [30, 1],
    [40, 2],
    [85, 6],
]

y = [
    "Pass",
    "Pass",
    "Fail",
    "Fail",
    "Pass"
]

model = DecisionTreeClassifier()

model.fit(x, y)

result = model.predict([[79, 0]])

print(result)