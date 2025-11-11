import cv2
import matplotlib.pyplot as plt


image = cv2.imread("ezc.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #cv2 stores as BGR matplot uses RGB this line converts
plt.imshow(image_rgb)
plt.title("RGB image")
plt.show()



gray_image = cv2.cvtColor(image, cv2.COLOR_BAYER_BG2GRAY)
plt.show(gray_image , cmap = "gray")
plt.title("Grayscale Image")
plt.show()




crop_image = image[100:300, 200:400]
crop_rgb = cv2.cvtColor(crop_image, cv2.COLOR_BGR2RGB)
plt.imshow(crop_rgb)
plt.title("Cropped Region")
plt.show()
