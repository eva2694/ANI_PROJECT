import cv2
from bottom_up import bottom_up

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


cv2.namedWindow("Original")
cv2.createTrackbar("distance", "Original", distance_trackbar, 100, updateValue_distance)
cv2.createTrackbar("angle", "Original", angle_trackbar, 100, updateValue_angle)

bottom_up = bottom_up()
original = cv2.imread('../selection/bikini_02s_13.jpg')
cv2.imshow('original', original)


def redraw():
  global bottom_up, distance_trackbar, angle_trackbar

  img = original.copy()
  final_coord_seqs = bottom_up.find_sequence(img, distance_trackbar, angle_trackbar)
  for seq in final_coord_seqs:
    [cv2.circle(img, (s[0], s[1]), 1, (0, 0, 255), -1) for s in seq]

  cv2.imshow('final', img)


redraw()
cv2.waitKey(0)
cv2.destroyAllWindows()
