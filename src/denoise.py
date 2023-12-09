import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors


def denoise(x, y, strategy):
  points = pd.DataFrame({'x': x, 'y': y}, dtype=int)
  if strategy == 'knn':
    points = remove_outliers_knn(points, k=3, min_connections=3, max_iter=1)
  elif strategy == 'radius':
    points = remove_outliers_radius(points, radius=20, min_connections=3, max_iter=1)
  elif strategy == 'graph':
    points = remove_small_graphs(points, k=3, min_size=10, max_iter=1)
  elif strategy == 'graph_ada':
    points = remove_small_graphs_adaptive(points, k=3, percent_to_keep=0.9, max_iter=2, strategy='mean')
  else:
    print(f"Unknown denoise strategy: {strategy}, not filtering points")
  print(f"Denoising with {strategy}. Keeping {len(points)} points out of {len(x)}")
  return points['x'].to_numpy(), points['y'].to_numpy()


def remove_outliers_knn(points, k=3, min_connections=2, max_iter=3):
  knn = NearestNeighbors(n_neighbors=k)

  for _ in range(max(1, max_iter)):
    knn.fit(points.values)
    connection_counts = knn.kneighbors_graph(points.values).toarray().sum(axis=0)
    points_to_keep = [points.iloc[i] for i, connections in enumerate(connection_counts) if
                      connections >= min_connections]
    points_to_keep = pd.concat(points_to_keep, axis=1).T

    if len(points_to_keep) == len(points):
      return points_to_keep
    points = points_to_keep

  return points_to_keep


def remove_outliers_radius(points, radius=10, min_connections=2, max_iter=3):
  knn = NearestNeighbors(radius=radius)

  for _ in range(max(1, max_iter)):
    knn.fit(points.values)
    connection_counts = knn.radius_neighbors_graph(points.values).toarray().sum(axis=0)
    points_to_keep = [points.iloc[i] for i, connections in enumerate(connection_counts) if
                      connections >= min_connections]
    points_to_keep = pd.concat(points_to_keep, axis=1).T

    if len(points_to_keep) == len(points):
      return points_to_keep
    points = points_to_keep

  return points_to_keep


def remove_small_graphs(points, k=3, min_size=10, max_iter=3):
  knn = NearestNeighbors(n_neighbors=k)

  for _ in range(max(1, max_iter)):
    knn.fit(points.values)
    connection_matrix = knn.kneighbors_graph(points.values).toarray().astype(int)
    graphs = find_connected_graphs(len(points), connection_matrix)
    point_idx_to_keep = np.unique([idx for g in graphs if len(g) >= min_size for idx in g])
    points_to_keep = [points.iloc[i] for i in point_idx_to_keep]
    points_to_keep = pd.concat(points_to_keep, axis=1).T

    if len(points_to_keep) == len(points):
      return points_to_keep
    points = points_to_keep

  return points_to_keep


def remove_small_graphs_adaptive(points, k=3, percent_to_keep=0.8, max_iter=3, strategy='mean'):
  knn = NearestNeighbors(n_neighbors=k)

  if strategy not in ['mean', 'min']:
    strategy = 'mean'

  for _ in range(max(1, max_iter)):
    knn.fit(points.values)
    connection_matrix = knn.kneighbors_graph(points.values).toarray().astype(int)
    graphs = find_connected_graphs(len(points), connection_matrix)
    sorted_sizes = sorted([len(g) for g in graphs], reverse=True)

    if strategy == 'mean':
      mean_of_top = np.mean(sorted_sizes[:int(len(graphs) * percent_to_keep)], dtype=int)
      point_idx_to_keep = np.unique([idx for g in graphs if len(g) >= mean_of_top for idx in g])
    elif strategy == 'min':
      min_of_top = min(sorted_sizes[:int(len(graphs) * percent_to_keep)])
      point_idx_to_keep = np.unique([idx for g in graphs if len(g) >= min_of_top for idx in g])

    points_to_keep = [points.iloc[i] for i in point_idx_to_keep]
    points_to_keep = pd.concat(points_to_keep, axis=1).T

    if len(points_to_keep) == len(points):
      return points_to_keep
    points = points_to_keep

  return points_to_keep


def find_connected_graphs(n_points, connection_matrix):
  visited = set()
  graphs = []
  for i in range(n_points):
    if i in visited:
      continue
    graph = find_graph_for_point(i, connection_matrix, [i])
    visited.update(graph)
    graphs.append(graph)
  return graphs


def find_graph_for_point(point_idx, connection_matrix, visited_points):
  connected_points = np.argwhere(connection_matrix[point_idx] == 1)
  for connected_idx in connected_points:
    if connected_idx not in visited_points:
      visited_points.append(connected_idx[0])
      find_graph_for_point(connected_idx[0], connection_matrix, visited_points)
  return visited_points
