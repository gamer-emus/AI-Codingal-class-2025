import cv2
import numpy as np



def apply_color_filter(image, filter_type):
    filtered_image = image.copy()


    if filter_type == "original":
        return filtered_image
    



    elif filter_type == "red_tint":
        filtered_image[:,:,1] = 0 #Green Channel First : represents first rows 2nd : represents colums
        filtered_image[:,:,0] = 0 #blue channel since 0 

    elif filter_type == "blue_tint":
        filtered_image[:,:,1] = 0 
        filtered_image[:,:,2] = 0 


    elif filter_type == "green_tint":
        filtered_image[:,:,0] = 0 
        filtered_image[:,:,2] = 0 
    
    elif filter_type == "increase_red":
        filtered_image[:,:,2] = cv2.add(filtered_image[:,:,2],50)

    elif filter_type == "Decreased_blue":
        filtered_image[:,:,0] = cv2.subtract(filtered_image[:,:,0],50)
    return filtered_image



image_path = "speed.jpeg"
image = cv2.imread(image_path)

if image is None:
    print("Error : image not found")
else:
    image = cv2.resize(image, (1200,800))


    filter_type = "Original"




    print("pRess the following keys to apply filters to your image")
    print("o - Original ")
    print("r - red tint")
    print("b - blue tint")
    print("g - green tint")
    print("i - increase Red intensity ")
    print("d - decrease blue intensity ")
    print("q - Quit")

    while True:
        key = cv2.waitKey(0) & 0xFF



        if key == ord("o"):
            filter_type = "original "
        elif key == ord("r"):
            filter_type = "red_tint"
        elif key == ord("b"):
            filter_type = "blue_tint"
        elif key == ord("g"):
            filter_type = "green_tint"
        elif key == ord("i"):
            filter_type = "increased_red"
        elif key == ord("d"):
            filter_type = "Decreased_blue"
        elif key == ord("q"):
            print("Exiting...")
            break
        else:
            print("Invalid key")


    cv2.destroyAllWindows()
