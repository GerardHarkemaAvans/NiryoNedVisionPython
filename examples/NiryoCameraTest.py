import time

from pyniryo2 import *
# import the opencv library
import keyboard  # load keyboard package

from libraries.vision.usbCamera import usbCamera
import libraries.niryo.NiryoSupport as Niryo


# The pose from where the image processing happens

def main():
    camera = usbCamera(0)

    robot = NiryoRobot("10.10.10.10")
    #robot.arm.reset_calibration()
    #robot.arm.request_new_calibration()
    robot.arm.calibrate_auto()

    robot.arm.set_learning_mode(False)

    #print("Enable TCP")

    #robot.tool.enable_tcp(False)
    #robot.tool.reset_tcp()

    print("To home pose")
    robot.arm.move_pose(Niryo.NED.HOME_POSE)

    print("To observation")
    robot.arm.move_pose(Niryo.NED.OBSERVATION_POSE)

    print("Take photo")
    camera.take_photo()

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
            camera.end();
            robot.end()
            print("You pressed q")
            time.sleep(0.5)
            break




if __name__ == "__main__":
    main()