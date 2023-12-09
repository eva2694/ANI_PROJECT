import cv2
import pandas as pd
from sklearn.neighbors import NearestNeighbors

from position_utils import find_dot_centres, stimuli_dots
from denoise import remove_outliers_knn


def draw_connections(image, points):
  for index, point in points.iterrows():
    neighbour_idxs = knn.kneighbors(point.values.reshape(1, -1), return_distance=False)[0]
    [cv2.line(image, point.values, points.iloc[ni].values, (0, 255), 1) for ni in neighbour_idxs]


def draw_filtered_points(image, filtered_points, color=(0, 0, 255)):
  [cv2.circle(image, point.values, 1, color, -1) for point in filtered_points]



original = cv2.imread('../selection/beaker_01b_13.jpg')
xs, ys = find_dot_centres(stimuli_dots(original))
df = pd.DataFrame({'x': xs, 'y': ys}, dtype=int)
k = 3
# depth = 3
# knn = NearestNeighbors(n_neighbors=k)
#
# cv2.imshow("original", original)
#
# for i in range(depth):
#   print(f"Iteration {i}, points: {len(df)}")
#   knn.fit(df.values)
#
#   connection_graph_img = original.copy()
#   filtered_points_img = original.copy()
#
#   draw_connections(connection_graph_img, df)
#
#   connection_matrix = knn.kneighbors_graph(df.values).toarray()
#   connection_counts = connection_matrix.sum(axis=0)
#   points_to_keep = [df.iloc[i] for i, connections in enumerate(connection_counts) if connections >= 2]
#
#   print(f"Keeping {len(points_to_keep)} points\n")
#   draw_filtered_points(connection_graph_img, points_to_keep)
#   draw_filtered_points(filtered_points_img, points_to_keep, color=(150, 200, 0))
#
#   df = pd.concat(points_to_keep, axis=1).T
#
#   cv2.imshow(f"connected iter {i}", connection_graph_img)
#   cv2.imshow(f"filtered iter {i}", filtered_points_img)
#   if cv2.waitKey(0) & 0xFF == ord('q'):
#     break
#   else:
#     continue

# cv2.destroyAllWindows()


filtered_points_img = original.copy()
points = remove_outliers_knn(df, k)
draw_filtered_points(filtered_points_img, points, color=(150, 200, 0))
cv2.imshow("original", original)
cv2.imshow(f"filtered", filtered_points_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
