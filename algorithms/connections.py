from collections import defaultdict

import numpy as np


def find_connections(seq):
  points = np.unique(np.array([np.array(p) for s in seq for p in s]), axis=0)
  index_by_dist = defaultdict(set)
  for i in range(len(points)):
    for j in range(min(i + 1, len(points) - 1), len(points)):
      d = int(np.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2))
      index_by_dist[d].update([(i, j)])
  keys = np.array(list(index_by_dist.keys()))
  keys = keys[keys < 20]
  counts = [len(index_by_dist[k]) for k in keys]
  mode = keys[np.argmax(counts)]
  keys = keys[(mode - 5 < keys) & (keys < mode + 5)]

  lines = []
  for k in keys:
    [lines.append(((points[p[0]]), (points[p[1]]))) for p in index_by_dist[k]]

  return lines
