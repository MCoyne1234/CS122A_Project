# USAGE
# python detect_shapes.py --image shapes_and_colors.png

# import the necessary packages
from pyimagesearch.shapedetector import ShapeDetector
import argparse
import imutils
import cv2
from picamera import PiCamera
from time import sleep
from pins import wheels
from multiprocessing import Process

def camProc():
    MIN_THRESH = .000001

    camera = PiCamera()
    camera.resolution = (640,480)
    camera.rotation = 180
    # construct the argument parse and parse the arguments
    #ap = argparse.ArgumentParser()
    #ap.add_argument("-i", "--image", required=True,
    #        help="path to the input image")
    #args = vars(ap.parse_args())

    # load the image and resize it to a smaller factor so that
    # the shapes can be approximated better

    #camera.start_preview()
    while True:
        sleep(2)
        camera.capture("./pic.jpg")
        #camera.stop_preview()

        image = cv2.imread("./pic.jpg")
        #image = cv2.imread(args["image"])

        resized = imutils.resize(image, width=300)
        ratio = image.shape[0] / float(resized.shape[0])

        # convert the resized image to grayscale, blur it slightly,
        # and threshold it
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.threshold(blurred, 111, 245, cv2.THRESH_BINARY_INV)[1]

        # find contours in the thresholded image and initialize the
        # shape detector
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        sd = ShapeDetector()

        # loop over the contours
        for c in cnts:
                # compute the center of the contour, then detect the name of the
                # shape using only the contour
            if cv2.contourArea(c) > MIN_THRESH:
                M = cv2.moments(c)
                cX = int((M["m10"] / M["m00"]) * ratio)
                cY = int((M["m01"] / M["m00"]) * ratio)
                shape = sd.detect(c)

                # multiply the contour (x, y)-coordinates by the resize ratio,
                # then draw the contours and the name of the shape on the image
                c = c.astype("float")
                c *= ratio
                c = c.astype("int")
                cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
                cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 255, 255), 2)

                # show the output image
                cv2.imshow("Image", image)
        cv2.waitKey(8000)
        cv2.destroyAllWindows()
        #cv2.waitKey(0)
        #return

def runInParallel(*fns):
  proc = []
  for fn in fns:
    p = Process(target=fn)
    p.start()
    proc.append(p)
  for p in proc:
    p.join()

if __name__ == '__main__':
    we = wheels()
    try:
        while True:
            runInParallel(we.gogo, camProc)
    except KeyboardInterrupt:
        pass