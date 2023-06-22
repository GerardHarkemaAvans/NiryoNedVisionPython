# import the opencv library
import keyboard  # load keyboard package

from libraries.vision.usbCamera import usbCamera
from libraries.vision.enums import *

def main():
    camera = usbCamera(CAMERA_INDEX)

    while True:
        if keyboard.is_pressed("q"):  # returns True if "q" is pressed
            camera.stop();
            print("You pressed q")
            break

        if keyboard.is_pressed("p"):  # returns True if "q" is pressed
            camera.take_photo();



if __name__ == "__main__":
    main()