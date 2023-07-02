# import the opencv library
import keyboard  # load keyboard package

from pyniryo2 import *
from libraries.vision.markers_detection import *
from libraries.vision.usbCamera import usbCamera
import libraries.niryo.NiryoSupport as Niryo
import cv2
import time
from libraries.vision.Workspace import Workspace
from libraries.vision.enums import *

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
def main():
    workspace = Workspace()
    robot = NiryoRobot("10.10.10.10")
    #robot.arm.reset_calibration()
    #robot.arm.request_new_calibration()
    robot.arm.calibrate_auto()

    robot.arm.set_learning_mode(False)

    print("To observation")
    robot.arm.move_pose(Niryo.NED.OBSERVATION_POSE)

    takePhoto()

    robot.tool.set_tcp(Niryo.NED.FINGER_GRIPPER_TCP_OFFSET)
    robot.tool.enable_tcp(True)

    cv2.waitKey(0)

    robot.arm.move_to_home_pose()
    robot.arm.set_learning_mode(True)

    print("Move to pose 1 and press enter")
    cv2.waitKey(0)
    pose1 = robot.arm.get_pose()
    print(pose1)

    print("Move to pose 2 and press enter")
    cv2.waitKey(0)
    pose2 = robot.arm.get_pose()
    print(pose2)

    print("Move to pose 3 and press enter")
    cv2.waitKey(0)
    pose3 = robot.arm.get_pose()
    print(pose3)

    print("Move to pose 4 and press enter")
    cv2.waitKey(0)
    pose4 = robot.arm.get_pose()
    print(pose4)

    workspace.set(pose1, pose2, pose3, pose4)
    with open('../workspace.json', 'w') as outfile:
        outfile.write(workspace.to_json())
    wsp = workspace.to_json()
    print(wsp)

    robot.tool.enable_tcp(False)

    camera.end();
    robot.end()
    time.sleep(0.5)

if __name__ == "__main__":
    main()