import cv2

# Importing image
image = cv2.imread('photos/camera.jpg')
# Resizing the image
resized = cv2.resize(image, (800, 800), interpolation=cv2.INTER_CUBIC)
image = resized

# Inverting  grayscale image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
inverted_image = 255 - gray_image

# Applying blur  by using the Gaussian Function
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
# Inverting the blurred image, so that we can easily convert the image into a pencil sketch
inverted_blurred = 255 - blurred

pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
#cv2.imshow("Sketch", pencil_sketch)
# cv2.waitKey(0)

# looking at both the original image and the pencil sketch
cv2.imshow("original image", image)
cv2.imshow("pencil sketch", pencil_sketch)

# Saving the sketched image !
cv2.imwrite('cameraSketch.jpg', pencil_sketch)

cv2.waitKey(0)
