from os import listdir
from os.path import join, isfile

import cv2
import numpy as np

from algorithms.connections import find_connections
from bottom_up import BottomUp
from conf import Conf


def draw_sequence_points(img, coord_seqs, color):
  for seq in coord_seqs:
    [cv2.circle(img, (s[0], s[1]), 1, color, -1) for s in seq]


def draw_sequences(img, coord_seqs, color):
  for seq in coord_seqs:
    for i in range(len(seq) - 1):
      cv2.line(img, (seq[i][0], seq[i][1]), (seq[i + 1][0], seq[i + 1][1]), color, 1)


def draw_used_points(img, x, y):
  [cv2.circle(img, point, 1, (0, 200, 100), -1) for point in zip(x, y)]


def draw_connections(img, coord_seq):
  lines = find_connections(coord_seq)
  [cv2.line(img, l[0], l[1], (0, 255, 0), 1) for l in lines]


def redraw(img, original_img):
  global conf

  bottom_up = BottomUp()
  denoised_img = original_img.copy()
  combined_img = original_img.copy()
  connections_img = original_img.copy()
  sequences_img = original_img.copy()

  combined_coord_seqs, xs, ys = bottom_up.find_sequence_denoise(original_img, conf.get_img_conf(img))
  draw_used_points(denoised_img, xs, ys)
  draw_sequence_points(combined_img, combined_coord_seqs, color=(200, 100, 0))
  draw_connections(connections_img, combined_coord_seqs)
  draw_sequences(sequences_img, combined_coord_seqs, color=(100, 200, 0))

  return denoised_img, combined_img, connections_img, sequences_img


images_dir = '../stimuli/selection'
save_dir = './connections'
images = [f for f in listdir(images_dir) if isfile(join(images_dir, f))]
conf = Conf()

for image in images:
  print(f"Image: {image}")
  original = cv2.imread(join(images_dir, image))

  denoised_img, combined_img, connections_img, sequences_img = redraw(image, original)

  cv2.imwrite(join(save_dir, f"dn_{image}"), denoised_img)
  cv2.imwrite(join(save_dir, f"co_{image}"), combined_img)
  cv2.imwrite(join(save_dir, f"co_lines_{image}"), connections_img)
  cv2.imwrite(join(save_dir, f"co_seq_{image}"), sequences_img)
  compare_dots_img = np.concatenate((denoised_img, combined_img), axis=1)
  compare_lines_img = np.concatenate((sequences_img, connections_img), axis=1)
  compare_all_img = np.concatenate((compare_dots_img, compare_lines_img), axis=0)
  cv2.imwrite(join(save_dir, f"compare_dots_{image}"), compare_dots_img)
  cv2.imwrite(join(save_dir, f"compare_lines_{image}"), compare_lines_img)
  cv2.imwrite(join(save_dir, f"compare_all_{image}"), compare_all_img)
