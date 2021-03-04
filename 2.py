import numpy as np
import cv2

img = cv2.imread('guava.jpg', 1)
img = cv2.line(img, (0, 0), (480, 0), (132, 66, 245), 45)
img = cv2.line(img, (0, 0), (0, 640), (57, 129, 221), 45)
img = cv2.line(img, (480, 0), (0, 500), (245, 167, 66), 45)
img = cv2.circle(img, (150, 150),80, (119, 25, 167), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'I love mom', (50,400),font, 2, (99, 66, 245), 1, cv2.LINE_AA)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()