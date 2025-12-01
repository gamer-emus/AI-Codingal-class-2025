import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title, image):
    """Utility function to display an image """
    plt.figure(figsize=(8,8))
    if len(image.shape) == 2:
        plt.imshow(image, cmap="gray")
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis("off")#displays image more clearly 
    plt.show()


def interactive_edge_detection(image_path):
    """Interactive activity for edge detection and filtering"""
    image= cv2.imread(image_path)
    if image is None:
        print("Error : image not found")
        return
    



    print("Select and option")
    print("1.sobel edge detection") #an image processing technique that identifies edges by detecting areas of rapid pixel intensity change. It uses a pair of \(3\times 3\) kernels (
    print("2.canny edge detection") #Canny edge detection is a multi-stage algorithm used in computer vision to identify edges in images by reducing noise, calculating gradients, and applying hysteresis thresholding to find the most significant edges.
    print("3.laplican edge detection") #Laplacian edge detection is an image processing technique that finds edges by computing the second-order derivative of an image's intensity.
    print("4.gaussing smoothing") #Gaussian smoothing is a process that uses a Gaussian function to average data points, resulting in a blurred effect that reduces noise and fine details
    print("5. median filtering") #A median filter is a digital filtering technique that removes noise by replacing each pixel or data point with the median value of its neighbors
    print("6. Exit")


    while True:
        choice = input("Enter your choice (1-6)")



        if choice == "1":
            sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0 ,ksize=3)
            sobely = cv2.Sobel(image , cv2.CV_64F , 0,1 , ksize=3) #1 detects verticle edges and 0 means horizontal thingy 
            combined_sobel = cv2.bitwise_or(sobelx.astype(np.uint8) , sobely.astype(np.uint8))
            display_image("Sobel image detection " , combined_sobel)

        elif choice == "2":
            print("Adjust thresholds for canny (default: 100 and 200)")
            lower_thresh = int(input("Enter lower thresholds : "))
            upper_thresh = int(input("Enter uper threshold: "))
            edges = cv2.Canny(image , lower_thresh, upper_thresh)
            display_image("Canny Edge detection" , edges)



        elif choice == "3":
            lapcian = cv2.Laplacian(image, cv2.CV_64F)
            display_image("Laplacian Edge Detection " , np.abs(lapcian).astype(np.uint8))

        elif choice == "4":
            print("Adjust kernal size for gaussin blur (must be a odd num default : 5)")
            kernal_size = int(input("Enter kernal size (odd number ):"))
            blurred = cv2.GaussianBlur(image , (kernal_size, kernal_size),0)
            display_image("Gaussin smoothed image " , blurred)

        elif choice == "5":
            print("adjust kernal size for median filttering (must be odd default 5:)")
            kernal_size = int(input("Enter kernal size (odd number ):"))
            median_filtered = cv2.medianBlur(image, kernal_size)
            display_image("Median filtered image ", median_filtered)
        
        elif choice == "6":
            print("Exitig...")
            return
        
        else:
            print("InValid choice select num between 1-6")


interactive_edge_detection("ezc.jpeg")
        

        






        









        






