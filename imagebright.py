import cv2
import matplotlib.pyplot as plt


image = cv2.imread("ezc.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #cv2 stores as BGR matplot uses RGB this line converts
plt.imshow(image_rgb)
plt.title("RGB image")
plt.show()

key = cv2.waitKey(0)

if key == ord("b"):
    cv2.imwrite("ezc.jpg" , image_rgb)
    print("Image saved as ezc.jpg")
else:
    print("Image not saved")











crop_image = image[100:300, 200:400]
crop_rgb = cv2.cvtColor(crop_image, cv2.COLOR_BGR2RGB)
plt.imshow(crop_rgb)
plt.title("Cropped Region")
plt.show()
