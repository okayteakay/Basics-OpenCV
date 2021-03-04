import cv2
import numpy as np

img = cv2.imread('lion.jpg',0)
_, th1 = cv2.threshold(img, 190, 255, cv2.THRESH_BINARY_INV)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

img = cv2.resize(img, (500, 300))
th1 = cv2.resize(th1, (500, 300))
th2 = cv2.resize(th2, (500, 300))
th3 = cv2.resize(th3, (500, 300))

cv2.imshow('image', img)
cv2.imshow('1', th1)
cv2.imshow('2', th2)
cv2.imshow('3', th3)

cv2.waitKey(0)
cv2.destroyAllWindows()