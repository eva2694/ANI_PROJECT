import cv2
import pandas as pd

from position_utils import find_dot_centres, stimuli_dots
from denoise import remove_outliers_knn, remove_outliers_radius, remove_small_graphs, remove_small_graphs_adaptive

original = cv2.imread('../stimuli/selection/padlock_06s_15.jpg')
xs, ys = find_dot_centres(stimuli_dots(original))
df = pd.DataFrame({'x': xs, 'y': ys}, dtype=int)


def draw_filtered_points(image, filtered_points, color=(0, 0, 255)):
  [cv2.circle(image, point, 1, color, -1) for point in filtered_points.values]


def test_denoiser(name, points, color):
  copy = original.copy()
  draw_filtered_points(copy, points, color=color)
  cv2.imshow(name, copy)


cv2.imshow("original", original)

points_knn = remove_outliers_knn(df, k=3, min_connections=3, max_iter=1)
points_radius = remove_outliers_radius(df, radius=20, min_connections=3, max_iter=1)
points_graph = remove_small_graphs(df, k=3, min_size=15)
points_adaptive_graph = remove_small_graphs_adaptive(df, k=3, percent_to_keep=0.9, max_iter=1, strategy='mean')

points_combined = remove_small_graphs_adaptive(df, k=3, percent_to_keep=0.9, max_iter=1, strategy='mean')
points_combined = remove_outliers_radius(points_combined, radius=18, min_connections=3, max_iter=5)

test_denoiser('knn', points_knn, color=(150, 200, 0))
test_denoiser('radius', points_radius, color=(200, 150, 0))
test_denoiser('graph fixed', points_graph, color=(200, 0, 150))
test_denoiser('graph adaptive', points_adaptive_graph, color=(0, 200, 150))
test_denoiser('combined', points_combined, color=(50, 100, 150))

cv2.waitKey(0)
cv2.destroyAllWindows()
