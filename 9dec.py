import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("speed.jpeg")

cv2.imshow("Original Image", image)
cv2.waitKey(0)   
cv2.destroyAllWindows()


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.imshow(gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")
plt.show()

cv2.waitKey(0)


cropped = image[100:300, 200:400]

cv2.imshow("Cropped Image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()



(h, w) = image.shape[:2]
center = (w // 2, h // 2)

matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, matrix, (w, h))

cv2.imshow("Rotated Image (45 degrees)", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()



brightness = 50
bright = cv2.add(image, brightness)

cv2.imshow("Brightened Image (+50)", bright)
cv2.waitKey(0)
cv2.destroyAllWindows()



cv2.imwrite("output_images/grayscale.jpg", gray)
cv2.imwrite("output_images/cropped.jpg", cropped)
cv2.imwrite("output_images/rotated.jpg", rotated)
cv2.imwrite("output_images/bright.jpg", bright)

print("All transformed images have been saved in output_images/")
