import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors


def remove_outliers_knn(points, k=3, min_connections=2, max_iter=3):
  """
  Every iteration removes points that have less than min_connections connections to other points. Uses Euclidean distance
  """
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
  """
  Every iteration removes points that have less than min_connections points in radius. Uses Euclidean distance.
  """
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


def remove_small_graphs(points, k=3, min_size=10):
  """
  Removes points that are in graphs smaller than min_size. Uses KNN to form graphs.
  """
  knn = NearestNeighbors(n_neighbors=k)

  knn.fit(points.values)
  connection_matrix = knn.kneighbors_graph(points.values).toarray().astype(int)
  graphs = find_connected_graphs(len(points), connection_matrix)
  point_idx_to_keep = np.unique([idx for g in graphs if len(g) >= min_size for idx in g])
  points_to_keep = [points.iloc[i] for i in point_idx_to_keep]
  return pd.concat(points_to_keep, axis=1).T


def remove_small_graphs_adaptive(points, k=3, percent_to_keep=0.8, max_iter=3, strategy='mean'):
  """
  Every iteration removes points that are in graphs smaller than defined by the strategy. Uses KNN to form graphs. Result will be the input for next iteration.
  Mean strategy: takes the mean size of top percent_to_keep graphs and removes all points in graphs smaller than that.
  Min strategy: takes the min size of top percent_to_keep graphs and removes all points in graphs smaller than that.
  """
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
    graph = find_graph_for_point(i, connection_matrix, {i})
    visited.update(graph)
    graphs.append(graph)
  return graphs


def find_graph_for_point(point_idx, connection_matrix, visited_points):
  connected_points = np.argwhere(connection_matrix[point_idx] == 1)
  for connected_idx in connected_points:
    if connected_idx[0] not in visited_points:
      visited_points.add(connected_idx[0])
      find_graph_for_point(connected_idx[0], connection_matrix, visited_points)
  return visited_points
