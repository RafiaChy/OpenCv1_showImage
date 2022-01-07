import cv2

img = cv2.imread('baboon.jpg', 1)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('Sample ', rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()
