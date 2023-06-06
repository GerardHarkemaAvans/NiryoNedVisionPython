from pyniryo import *
# import the opencv library
import keyboard  # load keyboard package

from libraries.vision.usbCamera import usbCamera
import libraries.niryo.NiryoSupportB as Niryo


# The pose from where the image processing happens

def main():
    #camera = usbCamera(0)

    robot = NiryoRobot("10.10.10.10")
    #robot.arm.reset_calibration()

    robot.calibrate_auto()

    robot.set_learning_mode(False)

    #print("Enable TCP")

    #robot.tool.enable_tcp(False)
    #robot.tool.reset_tcp()

    print("To home pose")
    robot.move_pose(Niryo.NED.HOME_POSE)

    print("To observation")
    robot.move_pose(Niryo.NED.OBSERVATION_POSE)

    print("Take photo")
    #camera.take_photo()

    print("Disable TCP")

    #robot.tool.set_tcp(Niryo.NED.FINGER_GRIPPER_TCP_OFFSET)
    #robot.tool.enable_tcp(True)

    test_pose = PoseObject(
        x=0.25, y=-0.1, z=0.02,
        roll=-0, pitch=0, yaw=0
    )

    print("To test pose")
    robot.move_pose(test_pose)

    #print("Disable TCP")
    #robot.tool.enable_tcp(False)
    #robot.tool.reset_tcp()

    print("To home pose")
    robot.move_pose(Niryo.NED.HOME_POSE)

    print("To resting pose")
    robot.move_to_home_pose()

    print("Ready")
    robot.set_learning_mode(True)

    while True:
        if keyboard.is_pressed("q"):  # returns True if "q" is pressed
            #camera.stop();
            robot.end()
            print("You pressed q")
            break




if __name__ == "__main__":
    main()