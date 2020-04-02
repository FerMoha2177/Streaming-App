import cv2

img = cv2.imread("mult.jpg", 1)  # image reading

# converting it into Hue, saturation, value (HSV)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  

# the : in an array in python means that we're going to slice that part of the array

h = hsv[:, :, 0]
s = hsv[:, :, 1]
v = hsv[:, :, 2]

hsv_split = np.concatenate((h, s, v), axis=1)
cv2.imshow("Split hsv", hsv_split) 

#  some of the values require multiple variables, hence why ret is shown multiple times

ret, min_sat = cv2.threshold(s, 40, 255, cv2.THRESH_BINARY)
#  showing an image is very simple, first argument is the name, second is the image we wish to show
cv2.imshow("Sat filter", min_sat) 

ret, max_hue = cv2.threshold(h, 15, 255, cv2.THRESH_BINARY_INV)  # will do the inverse of the normal threshold

cv2.imshow("Hue filter", max_hue)

# the final image is the min saturation and the max hue put together

final = cv2.bitwise_and(min_sat, max_hue)
cv2.imshow("Final", final)

cv2.imshow("Original image", img)

#  the windows will display until a key is pressed, this is using key characters, in this case we're using escape, which is 27 but 0 also works
cv2.waitKey(0)
#  destroy all windows will prevent you from having to mass spam the kill keys
cv2.destoryAllWindows()
