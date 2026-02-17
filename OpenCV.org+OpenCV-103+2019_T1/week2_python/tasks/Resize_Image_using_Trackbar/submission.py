import cv2

maxScaleUp = 100
scaleFactor = 1
scaleType = 0
maxType = 1

windowName = "Resize Image"
trackbarValue = "Scale"
trackbarType = "Type: \n 0: Scale Up \n 1: Scale Down"

# load an image
im = cv2.imread("./truth.png")

# Create a window to display results
cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)

def render():
    global scaleFactor
    global scaleType

    scaledImage = cv2.resize(im, None, fx=scaleFactor,\
            fy = scaleFactor, interpolation = cv2.INTER_LINEAR)
    cv2.imshow(windowName, scaledImage)

def updateScaleFactor(factor: float):
    global scaleFactor
    global scaleType

    scaleFactor = abs(((1 - scaleType) + (factor / 100.0)) - scaleType)

    if scaleFactor == 0:
        scaleFactor = 0.1

# Callback functions
def scaleImage(*args):
    global scaleFactor
    global scaleType

    updateScaleFactor(args[0])
    
    # Resize the image
    render()

# Callback functions
def scaleTypeImage(*args):
    global scaleType
    global scaleFactor
    scaleType = args[0]
    
    updateScaleFactor(scaleFactor)

    render()


cv2.createTrackbar(trackbarValue, windowName, scaleFactor, maxScaleUp, scaleImage)
cv2.createTrackbar(trackbarType, windowName, scaleType, maxType, scaleTypeImage)

cv2.imshow(windowName, im)
c = cv2.waitKey(0)

cv2.destroyAllWindows()
