import cv2
import math

rect_start = None
rect_end = None

source = cv2.imread("./sample.jpg",1)
frame = source.copy()


def drawRectangle(action, x, y, flags, userData):
    global rect_start, rect_end
    if action == cv2.EVENT_LBUTTONDOWN:
        rect_start = (x, y)
        rect_end = None

    elif action == cv2.EVENT_LBUTTONUP:
        rect_end = (x, y)

        x_start = min(rect_start[1], rect_end[1])
        y_start = min(rect_start[0], rect_end[0])
        x_end = max(rect_start[1], rect_end[1])
        y_end = max(rect_start[0], rect_end[0])

        cropted = source[x_start:x_end, y_start:y_end]
        cv2.imwrite("cropped.jpg", cropted)

cv2.namedWindow("Window")
# highgui function called when mouse events occur
cv2.setMouseCallback("Window", drawRectangle)
k = 0
# loop until escape character is pressed
while k != 27 :
    frame = source.copy()
    if rect_start and rect_end:
        cv2.rectangle(frame, rect_start, rect_end, (0,255,0), 2)

    cv2.imshow("Window", frame)
    cv2.putText(frame,'''Choose center, and drag, 
                      Press ESC to exit and c to clear''' ,
              (10,30), cv2.FONT_HERSHEY_SIMPLEX, 
              0.7,(255,255,255), 2 );
    k = cv2.waitKey(20) & 0xFF


cv2.destroyAllWindows()