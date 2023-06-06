import cv2
# import the opencv library
import keyboard  # load keyboard package
from libraries.vision.usbCamera import usbCamera
from libraries.vision.enums import ColorHSV
from libraries.vision.image_functions import *


def main():
    camera = usbCamera(1)

    while True:
        if keyboard.is_pressed("q"):  # returns True if "q" is pressed
            camera.stop();
            break

        if keyboard.is_pressed("p"):  # returns True if "q" is pressed
            image = camera.take_photo();

            (list_min_hsv, list_max_hsv, reverse_hue) = ColorHSV.BLUE
            hsv_image = threshold_hsv(image, list_min_hsv, list_max_hsv, reverse_hue)

            cv2.imshow("HSV", hsv_image)
            cv2.waitKey(1)


if __name__ == "__main__":
    main()