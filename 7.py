import cv2
import numpy as np

img1 = cv2.imread('traffic_sign.jpg')

print(img1.shape)
print(img1.size)
print(img1.dtype)

b,g,r = cv2.split(img1)
img1 = cv2.merge((b,g,r))

sign = img1[260:330, 715:790]
img1[270:340, 890:965] = sign

cv2.imshow('image', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()