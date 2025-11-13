import cv2


image = cv2.imread("ezc.jpg")



cv2.imshow("Og Image", image)

key = cv2.waitKey(0)


if key == ord('s'):
    resized_img = cv2.resize(image, (200, 200))
    cv2.imwrite("ezc_200.jpg", resized_img)
    cv2.imshow("Resized 200x200", resized_img)
    print("Image resized to 200x200 and saved as ezc_200.jpg")

elif key == ord('m'):
    resized_img = cv2.resize(image, (400, 400))
    cv2.imwrite("ezc_400.jpg", resized_img)
    cv2.imshow("Resized 400x400", resized_img)
    print("Image resized to 400x400 and saved as ezc_400.jpg")

elif key == ord('l') or key == ord('L'):
    resized_img = cv2.resize(image, (600, 600))
    cv2.imwrite("ezc_600.jpg", resized_img)
    cv2.imshow("Resized 600x600", resized_img)
    print("Image resized to 600x600 and saved as ezc_600.jpg")

else:
    print("No valid key pressed. Image not saved.")

cv2.waitKey(0)
cv2.destroyAllWindows()
