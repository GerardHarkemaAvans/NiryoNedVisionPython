# import the opencv library
import keyboard  # load keyboard package

from libraries.vision.usbCamera import usbCamera
from libraries.vision.enums import *
import easygui

def main():
    camera = usbCamera(1)
    image = None

    while True:
        if keyboard.is_pressed("q"):  # returns True if "q" is pressed
            camera.end();
            print("You pressed q")
            break

        if keyboard.is_pressed("p"):  # returns True if "p" is pressed
            image = camera.take_photo();

        if keyboard.is_pressed("s"):  # returns True if "p" is pressed
            if image != None:
                save_title = "Save the image as..."
                file_type = "*.jpg"
                output_path = easygui.filesavebox(title=save_title, default=file_type)
                cv2.imwrite(output_path, image)


if __name__ == "__main__":
    main()