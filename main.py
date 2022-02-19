import cv2
import numpy as np

# Functions needed for the code
def getColor(name, mask, color):
    contours, x = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.arcLength(cnt, True)
        if area > 100:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.putText(img, name, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 2)
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)

# HSV : HUE , SATURATION ,VALUE
# HUE: which corresponds the color component (from renge 0==>360)
# SATURATION: THE amount of color (depth of the pigment)
# Value: the brightness of the color 

def nothing(x):
    pass

#cap = cv2.VideoCapture(0)  # for using camera 

 # for the track bars for the image 
cv2.namedWindow("Tracking")
cv2.createTrackbar("LowerHue", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LowerSatu", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LowerValue", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UpperHue", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UpperSatu", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UpperValue", "Tracking", 255, 255, nothing)

while True:
    img = cv2.imread('Colors.jpg') # image to read
    #_, img = cap.read()   # for using camera for detection
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # convert the image to HSV image 
    
    # for ths slider for determine the lower & upper in HUE,SATURATION AND VALUE
            #=====>lower
    LowerHue = cv2.getTrackbarPos("LowerHue", "Tracking")
    LowerSaturation = cv2.getTrackbarPos("LowerSatu", "Tracking")
    LowerValue = cv2.getTrackbarPos("LowerValue", "Tracking")
            #=====>Upper 
    UpperHue = cv2.getTrackbarPos("UpperHue", "Tracking")
    UpperSaturation = cv2.getTrackbarPos("UpperSatu", "Tracking")
    UpperValue = cv2.getTrackbarPos("UpperValue", "Tracking")

     # lower &upper for HSV image 
    l_b = np.array([LowerHue, LowerSaturation, LowerValue])
    u_b = np.array([UpperHue, UpperSaturation, UpperValue])

# #Red
    l_b_red = np.array([175, 92, 40])
    u_b_red = np.array([232, 255, 255])
    mask_red = cv2.inRange(hsv, l_b_red, u_b_red)
    getColor("Red",mask_red,(0,0,255))
    #Green
    l_b_green = np.array([50, 64, 0])
    u_b_green = np.array([80, 255, 255])
    mask_green = cv2.inRange(hsv, l_b_green, u_b_green)
    l_b_lightGreen = np.array([35, 56, 163])
    u_b_lightGreen = np.array([52, 238, 255])
    mask_lightGreen = cv2.inRange(hsv, l_b_lightGreen, u_b_lightGreen)
    getColor("Green", mask_green, (50, 255, 0))
    getColor("Light Green", mask_lightGreen, (0, 255, 0))
    #Blue
    l_b_blue = np.array([104, 66, 47])
    u_b_blue = np.array([127, 255, 255])
    mask_blue = cv2.inRange(hsv, l_b_blue, u_b_blue)
    l_b_lightBlue = np.array([85, 106, 153])
    u_b_lightBlue = np.array([109, 255, 255])
    mask_lightBlue = cv2.inRange(hsv, l_b_lightBlue, u_b_lightBlue)
    getColor("Blue", mask_blue, (255, 0, 0))
    getColor("Light Blue", mask_lightBlue, (255, 100, 0))
    #Purple
    l_b_purple = np.array([134, 45, 66])
    u_b_purple = np.array([144, 224, 255])
    mask_purple = cv2.inRange(hsv, l_b_purple, u_b_purple)
    getColor("Purple", mask_purple, (255, 0, 200))
    #Pink
    l_b_pink = np.array([149, 101, 134])
    u_b_pink = np.array([170, 255, 255])
    mask_pink = cv2.inRange(hsv, l_b_pink, u_b_pink)
    getColor("Pink", mask_pink, (255, 0, 255))
    #Yellow
    l_b_yellow = np.array([16, 57, 130])
    u_b_yellow = np.array([35, 255, 255])
    mask_yellow = cv2.inRange(hsv, l_b_yellow, u_b_yellow)
    getColor("Yellow", mask_yellow, (0, 255, 255))
    #Orange
    l_b_orange = np.array([3, 78, 134])
    u_b_orange = np.array([23, 255, 255])
    mask_orange = cv2.inRange(hsv, l_b_orange, u_b_orange)
    getColor("Orange", mask_orange, (0, 165, 255))


    black_white = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(img, img, mask=black_white)

    cv2.imshow("original", img)
    cv2.imshow("result", res)

    i = cv2.waitKey(1)
    if i == 27:
        break
#cap.release()
cv2.destroyAllWindows()