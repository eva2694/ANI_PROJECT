import cv2
import matplotlib.pyplot as plt

from position_utils import *

img = cv2.imread('../selection/beaker_01b_13.jpg')
x, y = find_dot_centres(stimuli_dots(img))
print(x, y)

for i in range(len(x)):
  cv2.circle(img, (int(x[i]), int(y[i])), 1, (0, 0, 255), -1)

plt.hist(y, bins=40)
plt.show()

cv2.imshow('final', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
