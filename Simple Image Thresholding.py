import cv2 as cv 
import numpy as np

img = cv.imread('gradient.png', 0)

_,Th1 = cv.threshold(img, 55, 255, cv.THRESH_BINARY)
_,Th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
_,Th3 = cv.threshold(img, 127 , 255, cv.THRESH_TRUNC)
_,Th4 = cv.threshold(img , 127, 255, cv.THRESH_TOZERO)
_,Th5 = cv.threshold(img , 127, 255, cv.THRESH_TOZERO_INV)


cv.imshow('Image', img)
cv.imshow('Th1', Th1)
cv.imshow('Th2', Th2)
cv.imshow('Th3', Th3)
cv.imshow('Th4', Th4)
cv.imshow('Th5', Th5)



cv.waitKey(0)
cv.destroyAllWindows()

