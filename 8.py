import cv2
import numpy as np

img1 = cv2.imread('art.jpg')
img2 = cv2.imread('glass_building.jpg')

b,g,r = cv2.split(img1)
img1 = cv2.merge((b,g,r))

img1 = cv2.resize(img1, (512, 512))
img2 = cv2.resize(img2, (512, 512))

final1 = cv2.add(img1, img2)
final2 = cv2.addWeighted(img1, 0.4, img2, 0.6, 0)

cv2.imshow('final image1', final1)
cv2.imshow('final image2', final2)

cv2.waitKey(0)
cv2.destroyAllWindows()