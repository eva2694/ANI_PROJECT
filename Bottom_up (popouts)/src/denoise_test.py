import cv2
import pandas as pd

from position_utils import find_dot_centres, stimuli_dots
from denoise import remove_outliers_knn, remove_outliers_radius, remove_small_graphs


def draw_filtered_points(image, filtered_points, color=(0, 0, 255)):
  [cv2.circle(image, point, 1, color, -1) for point in filtered_points.values]


original = cv2.imread('../selection/padlock_06s_15.jpg')
xs, ys = find_dot_centres(stimuli_dots(original))
df = pd.DataFrame({'x': xs, 'y': ys}, dtype=int)

knn_points_img = original.copy()
radius_points_img = original.copy()
graph_points_img = original.copy()

points_knn = remove_outliers_knn(df, k=3, min_connections=3, max_iter=1)
points_radius = remove_outliers_radius(df, radius=20, min_connections=3, max_iter=1)
points_graph = remove_small_graphs(df, k=3, min_size=15, max_iter=2)

draw_filtered_points(knn_points_img, points_knn, color=(150, 200, 0))
draw_filtered_points(radius_points_img, points_radius, color=(200, 150, 0))
draw_filtered_points(graph_points_img, points_graph, color=(200, 0, 150))

cv2.imshow("original", original)
cv2.imshow(f"filtered knn", knn_points_img)
cv2.imshow(f"filtered radius", radius_points_img)
cv2.imshow(f"graph points", graph_points_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
