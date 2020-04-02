import cv2

print("OPENCV VERSOIN:  ", cv2.__version__)

#load image
img = cv2.imread("Sassy.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#show the image
cv2.imshow("Sassy", img)
cv2.imshow("Sassy-gray", img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
