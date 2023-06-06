import cv2
# import the opencv library
import keyboard  # load keyboard package
import time
from libraries.vision.usbCamera import usbCamera
from libraries.vision.markers_detection import *


def main():
    camera = usbCamera(1)

    while True:
        if keyboard.is_pressed("q"):  # returns True if "q" is pressed
            camera.stop();
            break

        if keyboard.is_pressed("p"):  # returns True if "q" is pressed
            image = camera.take_photo(display_photo=False);
            result = False
            result, crop_image = extract_img_markers(image, workspace_ratio=1.0)
            if result:
                cv2.imshow("Crop", crop_image)
            else:
                print("Unable to extract image markers")

            result, marker_image = draw_markers(image, workspace_ratio=1.0)
            if result:
                cv2.imshow("Marker", marker_image)
            else:
                print("Unable to draw image markers")

            cv2.waitKey(1)
            time.sleep(1)

if __name__ == "__main__":
    main()