import imutils
import cv2

# read and show
image = cv2.imread("GOT.jpeg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

cv2.imshow("Image", image)
cv2.waitKey(0)

# pixel
(B, G, R) = image[100, 50]
print("PIXEL: R={}, G={}, B={}".format(R, G, B))

# crop
varys = image[60:160, 280:400]  # image[startY:endY, startX:endX]
cv2.imshow("VARYS", varys)
cv2.waitKey(0)

# resize
resized = cv2.resize(image, (300, 300))
cv2.imshow("Fixed Resizing", resized)
cv2.waitKey(0)

# resize with aspect ratio
r = 300.0 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
print(f"Resized shape: {resized.shape}")
cv2.imshow("Aspect Ratio Resize", resized)
cv2.waitKey(0)

# Resize with imutils
resized = imutils.resize(image, width=300)
cv2.imshow("Imutils Resize", resized)
cv2.waitKey(0)

# Rotation
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("OpenCV Rotation", rotated)
cv2.waitKey(0)

# Rotation with imutils
rotated = imutils.rotate(image, -45)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)

# Rotation with imutils (keep whole image)
rotated = imutils.rotate_bound(image, 45)
cv2.imshow("Imutils Bound Rotation", rotated)
cv2.waitKey(0)

# image smoothing
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)

# drawing on image
# rectangle
output = image.copy()
cv2.rectangle(output, (320, 40), (380, 120), (0, 0, 255), 2)  # (LEFT W, H), (RIGHT W, H)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)

# circle
output = image.copy()
cv2.circle(output, (500, 350), 20, (255, 0, 0), -1)
cv2.imshow("Circle", output)
cv2.waitKey(0)

# line
output = image.copy()
cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)
cv2.imshow("Line", output)
cv2.waitKey(0)

# Text
output = image.copy()
cv2.putText(output, "OpenCV + Game of Thrones!!!", (10, 25),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)
