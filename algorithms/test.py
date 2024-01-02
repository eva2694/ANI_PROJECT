from collections import defaultdict
from os import listdir
from os.path import join, isfile

import cv2
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from scipy import stats

from bottom_up import BottomUp
from conf import Conf


def update(img, key, val, original_img):
  global conf, redraw_ready
  conf.set(img, key, val)
  if redraw_ready:
    redraw(img, original_img)


def draw_sequence(img, coord_seqs, color):
  for seq in coord_seqs:
    [cv2.circle(img, (s[0], s[1]), 1, color, -1) for s in seq]
    for i in range(len(seq) - 1):
      cv2.line(img, (seq[i][0], seq[i][1]), (seq[i + 1][0], seq[i + 1][1]), color, 1)


def draw_neighbours(image, points):
  knn = NearestNeighbors(n_neighbors=3)
  knn.fit(points.values)
  for index, point in points.iterrows():
    neighbour_idxs = knn.kneighbors(point.values.reshape(1, -1), return_distance=False)[0]
    [cv2.line(image, point.values, points.iloc[ni].values, (0, 255), 1) for ni in neighbour_idxs]


def draw_connections(seq, img):
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
  keys = keys[(mode - 4 < keys) & (keys < mode + 4)]

  for k in keys:
    for p in index_by_dist[k]:
      cv2.line(img, (points[p[0]]), (points[p[1]]), (0, 255, 0), 1)


def draw_used_points(img, x, y):
  [cv2.circle(img, point, 1, (0, 255, 0), -1) for point in zip(x, y)]


def redraw(img, original_img):
  global conf

  bottom_up = BottomUp()
  denoised_img = original_img.copy()
  combined_img = original_img.copy()
  connections_img = original_img.copy()

  combined_coord_seqs, xs, ys = bottom_up.find_sequence_denoise(original_img, conf.get_img_conf(img))
  draw_used_points(denoised_img, xs, ys)
  draw_sequence(combined_img, combined_coord_seqs, color=(255, 0, 255))
  # draw_neighbours(denoised_img, pd.DataFrame({'x': xs, 'y': ys}, dtype=int))
  draw_connections(combined_coord_seqs, connections_img)

  cv2.imshow('denoised', denoised_img)
  cv2.imshow('combined', combined_img)
  cv2.imshow('connections', connections_img)
  return denoised_img, combined_img


def create_trackbars(img, conf, original_img):
  global redraw_ready

  redraw_ready = False
  for key in conf.keys():
    cv2.createTrackbar(key, "Conf", conf.get(img, key), conf.max_val(key),
                       (lambda v, i=img, k=key, o=original_img: update(img=i, key=k, val=v, original_img=o)))
  redraw_ready = True


images_dir = '../stimuli/selection'
save_dir = './out'
images = [f for f in listdir(images_dir) if isfile(join(images_dir, f))]
conf = Conf()
redraw_ready = False

for image in images:
  print(f"Image: {image}")
  cv2.namedWindow("Conf")
  original = cv2.imread(join(images_dir, image))
  create_trackbars(image, conf, original)
  cv2.imshow(f'original {image}', original)
  denoised_img, combined_img = redraw(image, original)

  if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.imwrite(join(save_dir, f"dn_{image}"), denoised_img)
    cv2.imwrite(join(save_dir, f"co_{image}"), combined_img)
    break
  else:
    cv2.destroyWindow(f'original {image}')
    cv2.destroyWindow("Conf")
    cv2.imwrite(join(save_dir, f"dn_{image}"), denoised_img)
    cv2.imwrite(join(save_dir, f"co_{image}"), combined_img)
    continue

cv2.destroyAllWindows()
conf.save()
