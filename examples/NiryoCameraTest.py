import time

from pyniryo2 import *
import cv2
# import the opencv library
import keyboard  # load keyboard package
from libraries.vision.markers_detection import *
from libraries.vision.usbCamera import usbCamera
import libraries.niryo.NiryoSupport as Niryo
from libraries.vision.enums import *


# The pose from where the image processing happens

camera = usbCamera(CAMERA_INDEX)
def takePhoto():
    image = camera.take_photo()
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
def main():


    robot = NiryoRobot("10.10.10.10")
    #robot.arm.reset_calibration()
    robot.arm.request_new_calibration()
    robot.arm.calibrate_auto()

    robot.arm.set_learning_mode(False)

    #print("Enable TCP")

    robot.tool.enable_tcp(False)
    #robot.tool.reset_tcp()

    print("To home pose")
    #robot.arm.move_pose(Niryo.NED.HOME_POSE)

    print("To observation")
    robot.arm.move_pose(Niryo.NED.OBSERVATION_POSE)

    print("Take photo")
    takePhoto()

    print("Disable TCP")

    robot.tool.set_tcp(Niryo.NED.FINGER_GRIPPER_TCP_OFFSET)
    robot.tool.enable_tcp(True)

    test_pose = PoseObject(
        x=0.15, y=-0.1, z=0.10,
        roll=-1.57, pitch=1.5, yaw=-1.57
    )

    print("To test pose with tcp")
    robot.arm.move_pose(test_pose)

    print("Disable TCP")
    robot.tool.enable_tcp(False)
    robot.tool.reset_tcp()

    print("To test pose without tcp")
    robot.arm.move_pose(test_pose)

    print("To home pose")
    robot.arm.move_pose(Niryo.NED.HOME_POSE)

    print("To resting pose")
    robot.arm.move_to_home_pose()

    print("Ready")
    robot.arm.set_learning_mode(True)

    while True:
        if keyboard.is_pressed("q"):  # returns True if "q" is pressed
            robot.arm.move_to_home_pose()
            robot.arm.set_learning_mode(True)
            camera.end();
            robot.end()
            time.sleep(0.5)
            break
        if keyboard.is_pressed("o"):  # returns True if "o" is pressed
            print("To observation")
            robot.arm.set_learning_mode(False)
            robot.arm.move_pose(Niryo.NED.OBSERVATION_POSE)
            camera.enable_crosshair(True)
            time.sleep(0.5)
        if keyboard.is_pressed("r"):  # returns True if "o" is pressed
            print("To resting pose")
            robot.arm.move_to_home_pose()
            robot.arm.set_learning_mode(True)
            time.sleep(0.5)
        if keyboard.is_pressed("p"):  # returns True if "o" is pressed
            print("Take photo")
            takePhoto()
            time.sleep(0.5)




if __name__ == "__main__":
    main()