from sklearn.cluster import KMeans

x = [
    [90, 5],
    [80, 4],
    [30, 1],
    [40, 2],
    [85, 6],
]

model = KMeans(n_clusters=3, random_state=1)
model.fit(x)

for point, cluster in zip(x, model.labels_):
    print(point, "-> Cluster", cluster)