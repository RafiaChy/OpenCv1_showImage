import cv2

img = cv2.imread('baboon.jpg', 0)
cv2.imshow('Sample ', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
