import cv2
import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.neighbors import NearestNeighbors

from position_utils import *


def connect_neighbours(image, points):
  for index, point in points.iterrows():
    x = point.iloc[0]
    y = point.iloc[1]
    neighbour_idxs = knn.kneighbors(point.values.reshape(1, -1), return_distance=False)[0]
    for i in neighbour_idxs:
      nx = points.iloc[i, 0]
      ny = points.iloc[i, 1]
      cv2.line(image, (x, y), (nx, ny), (0, 255), 1)


original = cv2.imread('../selection/beaker_01b_13.jpg')
xs, ys = find_dot_centres(stimuli_dots(original))
print(len(xs), len(ys))
df = pd.DataFrame({'x': xs, 'y': ys}, dtype=int)

# TODO test with radius
k = 3
knn = NearestNeighbors(n_neighbors=k)
knn.fit(df.values)

connection_graph_img = original.copy()
filtered_points_img = original.copy()

connect_neighbours(connection_graph_img, df)

connection_matrix = knn.kneighbors_graph(df).toarray()
[cv2.circle(connection_graph_img, (df.iloc[i, 0], df.iloc[i, 1]), 1, (0, 0, 255), -1) for i, connections in enumerate(connection_matrix.sum(axis=0)) if connections >= 2]

points_to_keep = [df.iloc[i] for i, connections in enumerate(connection_matrix.sum(axis=0)) if connections >= 2]
print(len(points_to_keep))
points = pd.concat(points_to_keep, axis=1).T
[cv2.circle(filtered_points_img, (point.iloc[0], point.iloc[1]), 1, (100, 200, 0), -1) for index, point in points.iterrows()]


cv2.imshow('final', original)
cv2.imshow('connected', connection_graph_img)
cv2.imshow('filtered', filtered_points_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
