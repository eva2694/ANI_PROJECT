import cv2
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors

from denoise import find_connected_graphs
from position_utils import find_dot_centres, stimuli_dots


def random_color():
  return np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)


def draw_neighbours(image, points, knn):
  for index, point in points.iterrows():
    neighbour_idxs = knn.kneighbors(point.values.reshape(1, -1), return_distance=False)[0]
    [cv2.line(image, point.values, points.iloc[ni].values, (0, 255), 1) for ni in neighbour_idxs]


def draw_filtered_points(image, filtered_points, color=(0, 0, 255)):
  [cv2.circle(image, point, 1, color, -1) for point in filtered_points.values]


def draw_graph(image, graph, points, color=(0, 200, 200)):
  [cv2.circle(image, point, 1, color, -1) for point in points.iloc[graph].values]


original = cv2.imread('../selection/padlock_06s_15.jpg')
xs, ys = find_dot_centres(stimuli_dots(original))
df = pd.DataFrame({'x': xs, 'y': ys}, dtype=int)
k = 3
depth = 2

cv2.imshow("original", original)

for i in range(depth):
  print(f"Iteration {i}, points: {len(df)}")
  knn = NearestNeighbors(n_neighbors=k+i)
  knn.fit(df.values)

  connection_graph_img = original.copy()
  filtered_points_img = original.copy()
  graphs_img = original.copy()
  graph_points_img = original.copy()

  draw_neighbours(connection_graph_img, df, knn)

  connection_matrix = knn.kneighbors_graph(df.values).toarray().astype(int)
  graphs = find_connected_graphs(len(df), connection_matrix)
  sorted_sizes = sorted([len(g) for g in graphs], reverse=True)
  print(sorted_sizes)
  print(sorted_sizes[:int(len(graphs) * 0.7)])
  # mean_of_top = np.mean(sorted_sizes[:int(len(graphs) * 0.7)], dtype=int)
  min_of_top = min(sorted_sizes[:int(len(graphs) * 0.7)])
  print(min_of_top)


  [draw_graph(graphs_img, graph, df, color=random_color()) for i, graph in enumerate(graphs)]
  graph_filtered = np.unique([idx for g in graphs if len(g) > min_of_top for idx in g])
  draw_graph(graph_points_img, graph_filtered, df)

  connection_counts = connection_matrix.sum(axis=0)
  # points_to_keep = [df.iloc[i] for i, connections in enumerate(connection_counts) if connections >= 2]
  points_to_keep = [df.iloc[i] for i in graph_filtered]
  points_to_keep = pd.concat(points_to_keep, axis=1).T

  print(f"Keeping {len(points_to_keep)} points\n")
  draw_filtered_points(connection_graph_img, points_to_keep)
  draw_filtered_points(filtered_points_img, points_to_keep, color=(150, 200, 0))

  df = points_to_keep

  cv2.imshow(f"connected iter {i}", connection_graph_img)
  cv2.imshow(f"filtered iter {i}", filtered_points_img)
  cv2.imshow(f"graphs iter {i}", graphs_img)
  cv2.imshow(f"graph points iter {i}", graph_points_img)
  if cv2.waitKey(0) & 0xFF == ord('q'):
    break
  else:
    continue

cv2.destroyAllWindows()
