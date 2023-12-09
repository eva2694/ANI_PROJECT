import cv2
import pandas as pd

from bottom_up import bottom_up, find_dot_centres, stimuli_dots

distance_trackbar = 25
angle_trackbar = 10


def updateValue_distance(new_distance):
  global distance_trackbar
  distance_trackbar = new_distance
  redraw()


def updateValue_angle(new_angle):
  global angle_trackbar
  angle_trackbar = new_angle
  redraw()


def draw_sequence(img, final_coord_seqs):
  for seq in final_coord_seqs:
    [cv2.circle(img, (s[0], s[1]), 1, (100, 0, 200), -1) for s in seq]


def draw_used_points(img, x, y):
  [cv2.circle(img, point, 1, (0, 200, 100), -1) for point in zip(x, y)]


cv2.namedWindow("Original")
cv2.createTrackbar("distance", "Original", distance_trackbar, 100, updateValue_distance)
cv2.createTrackbar("angle", "Original", angle_trackbar, 100, updateValue_angle)

bottom_up = bottom_up()
original = cv2.imread('../selection/bikini_02s_13.jpg')
cv2.imshow('original', original)


def redraw():
  global bottom_up, distance_trackbar, angle_trackbar

  final_img = original.copy()
  used_points_img = original.copy()

  final_coord_seqs, xs, ys = bottom_up.find_sequence(original, distance_trackbar, angle_trackbar, 'graph_ada')
  draw_used_points(used_points_img, xs, ys)
  draw_sequence(final_img, final_coord_seqs)

  cv2.imshow('final', final_img)
  cv2.imshow('used points', used_points_img)


redraw()
cv2.waitKey(0)
cv2.destroyAllWindows()
