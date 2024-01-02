import cv2
import matplotlib.pyplot as plt
from PIL import Image

# plot with 4 images in 2 rows
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# images = ['./out/denoise/graph_adaptive_50_giraffe_20s_15.jpg.jpg',
#           './out/denoise/graph_adaptive_80_giraffe_20s_15.jpg.jpg',
#           './out/denoise/graph_adaptive_50_bag_04s_11.jpg.jpg',
#           './out/denoise/graph_adaptive_80_bag_04s_11.jpg.jpg']
# title = ["giraffe 50%", "giraffe 80%", "bag 50%", "bag 80%"]

# images = ['./out/denoise/knn_3_bag_04s_11.jpg',
#           './out/denoise/knn_3_2_bag_04s_11.jpg',
#           './out/denoise/knn_4_bag_04s_11.jpg',
#           './out/denoise/knn_4_2_bag_04s_11.jpg']
# title = ["bag k=3 connections=1", "bag k=3 connections=2", "bag k=4 connections=1", "bag k=4 connections=2"]

# images = ['./out/denoise/radius_15_2_bag_04s_11.jpg',
#           './out/denoise/radius_15_3_bag_04s_11.jpg',
#           './out/denoise/radius_10_2_bag_04s_11.jpg',
#           './out/denoise/radius_10_3_bag_04s_11.jpg']
# title = ["bag radius=15 connections=2", "bag radius=15 connections=3", "bag radius=10 connections=2", "bag radius=10 connections=3"]

# images = ['./out/denoise/graph_fixed_10_giraffe_20s_15.jpg.jpg',
#           './out/denoise/graph_fixed_15_giraffe_20s_15.jpg.jpg',
#           './out/denoise/graph_fixed_15_bag_04s_11.jpg.jpg',
#           './out/denoise/graph_fixed_10_bag_04s_11.jpg.jpg']
# title = ["giraffe threshold=10", "giraffe threshold=15", "bag threshold=15", "bag threshold=20"]

# images = ['../stimuli/solutions/bag_04s.jpg',
#           '../screenshots/Annu_trial14_screenshot14.png',
#           './out/bu_bag_04s_11.jpg',
#           './out/dn_bag_04s_11.jpg']
# title = ["bag original outline", "bag human guess", "bag existing algorithm", "bag graph + radius filter"]

images = ['../stimuli/solutions/giraffe_20s.jpg',
          '../screenshots/Melon Eier_trial7_screenshot7.png',
          './out/bu_giraffe_20s_15.jpg',
          './out/dn_giraffe_20s_15.jpg']
title = ["giraffe original outline", "giraffe human guess", "giraffe existing algorithm", "giraffe graph + radius filter"]

for i, image in enumerate(images):
  img = Image.open(image)
  plt.subplot(2, 2, i + 1)
  plt.title(title[i])
  plt.axis("off")
  plt.imshow(img)

plt.subplots_adjust(hspace=0.1, wspace=0.1)
plt.show()
fig.savefig('./out/denoise/graph_fixed.jpg', bbox_inches='tight', pad_inches=0.2)
