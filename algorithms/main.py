from os import listdir
from os.path import join, isfile

import cv2

from bottom_up import BottomUp
from conf import Conf


def update(img, key, val, original_img):
  global conf, redraw_ready
  conf.set(img, key, val)
  if redraw_ready:
    redraw(img, original_img)


def draw_sequence(img, final_coord_seqs):
  for seq in final_coord_seqs:
    [cv2.circle(img, (s[0], s[1]), 1, (100, 0, 200), -1) for s in seq]


def draw_used_points(img, x, y):
  [cv2.circle(img, point, 1, (0, 200, 100), -1) for point in zip(x, y)]


def redraw(img, original_img):
  global conf

  bottom_up = BottomUp()
  bottom_up_img = original_img.copy()
  denoised_img = original_img.copy()

  final_coord_seqs, xs, ys = bottom_up.find_sequence(original_img, conf.get_img_conf(img))
  draw_used_points(denoised_img, xs, ys)
  draw_sequence(bottom_up_img, final_coord_seqs)

  cv2.imshow('bottom up', bottom_up_img)
  cv2.imshow('denoised', denoised_img)


def create_trackbars(img, conf, original_img):
  global redraw_ready

  redraw_ready = False
  for key in conf.keys():
    cv2.createTrackbar(key, "Conf", conf.get(img, key), conf.max_val(key),
                       (lambda v, i=img, k=key, o=original_img: update(img=i, key=k, val=v, original_img=o)))
  redraw_ready = True


images_dir = '../stimuli/selection'
images = [f for f in listdir(images_dir) if isfile(join(images_dir, f))]
conf = Conf()
redraw_ready = False

for image in images:
  print(f"Image: {image}")
  cv2.namedWindow("Conf")
  original = cv2.imread(join(images_dir, image))
  create_trackbars(image, conf, original)
  cv2.imshow(f'original {image}', original)
  redraw(image, original)

  if cv2.waitKey(0) & 0xFF == ord('q'):
    break
  else:
    cv2.destroyWindow(f'original {image}')
    cv2.destroyWindow("Conf")
    continue

cv2.destroyAllWindows()
conf.save()
