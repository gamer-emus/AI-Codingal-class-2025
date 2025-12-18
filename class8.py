import cv2
import numpy as np
from datetime import datetime



def apply_filters(image , ftype):
    img = image.copy()
    if image == "red_tint":
        img[:,:,1] = img[:,:,0] = 0
    elif image == "green_tint":
        img[:,:,0] = img[:,:,2]
    elif image == "blue_tint":
        img[:,:,1] = img[:,:,2]
    elif ftype == "sobel":
        gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
        sx = cv2.convertScaleAbs(cv2.Sobel(gray,cv2.CV_64F , 1,0 , ksize = 3))
        sy = cv2.convertScaleAbs(cv2.Sobel(gray , cv2.CV_64F , 1 , 0 , ksize= 3))
        sob = cv2.addWeighted(sx , 0.5 , sy , 0.5)
        img = cv2.cvtColor(sob, cv2.COLOR_GRAY2BGR)
    elif ftype == "canny":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        img = cv2.cvtColor(cv2.canny(gray , 100 , 200 ), cv2.COLOR_GRAY2BGR)
    elif ftype == "cartoon":
        gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray , 5 )
        edges = cv2.adaptiveThreshold(gray , 255, cv2.ADAPTIVE_THRESH_MEAN_C ,cv2.THRESH_BINARY, 9,9)
        color = cv2.bilateralFilter(9,300,300)
        img = cv2.bitwise_and(color, color, mask=edges)
    return img
def draw_intructions(frame):
    h , w = frame.shape[:2]
    overlay = frame.copy()
    cv2.rectangle(overlay, (10,10), (280,240), (0,0,0), -1)
    cv2.addWeighted(overlay, 0.6, frame , 0.4, 0,frame)
    instructions = [
        "Controls:",
        "R- Red tint",
        "G- Green tint",
        "B - Blue Tint",
        "S - Sobel edge"
        "C- cannt edge",
        "T - Cartoon",
        "o - Original",
        "P - screenshot"
        "Q - quit"


    ]

    for i , text in enumerate(instructions):
        color = (0,255,255) if i == 0 else(255,255,255)
        thickness = 2 if i == 0 else 1
        cv2.putText(frame, text , (20,35 + i*20), cv2.FONT_HERSHEY_SIMPLEX , 0.5 , color , thickness)
    def ss(frame, filter_name):
        timestamp = datetime.now().strftime("%Y%m%d_#H%M%S")
        filename = f"screenshot_{filter_name}_{timestamp}.jpg"
        cv2.imwrite(filename , frame)
        print(f"✅ Screenshot Saved {filename}")
        return filename
    def main():
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            print("X: Camera can not be opened")
            return
        ftype = "Original"
        print("Camera started ")
        while True:
            ret, frame  = cap.read()
            if not ret:
                break
            frame = cv2.flip(frame , 1)
            out = frame.copy() if ftype == "Original" else apply_filters(frame , ftype)
            draw_intructions(out)
            

            filter_display = ftype.replace("_, ").upper()
            cv2.putText(out , f"Filter {filter_display}" ,(10, out.shape[0]-20),cv2.FONT_HERSHEY_SIMPLEX, 0.7 , (0,255, 0), 2 )
            cv2.imshow("Real-time FIlters",out)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("r"):
                ftype = "red_tint"
            elif key == ord("g"):
                ftype = "green_tint"
            elif key == ord("b"):
                ftype = "blue_tint"
            elif key == ord("s"):
                ftype = "sobel"
            elif key == ord("c"):
                ftype = "canny"
            elif key == ord("t"):
                ftype = "cartoon"
            elif key == ord("o"):
                ftype = "original"
            elif key == ord("p"):
                ss(out,ftype)
            elif key == ord("q"):
                break
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
            



        

    
    