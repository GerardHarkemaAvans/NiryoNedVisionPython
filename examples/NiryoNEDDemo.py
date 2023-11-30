import time
from pyniryo2 import *

def main():

    #define poses
    home_pose = PoseObject(
        x=0.25, y=0.0, z=0.4,
        roll=-1.571, pitch=1.571, yaw=-1.571
    )
    left_pose = PoseObject(
        x=0.25, y=-0.2, z=0.4,
        roll=-1.571, pitch=1.571, yaw=-1.571
    )
    right_pose = PoseObject(
        x=0.25, y=0.2, z=0.4,
        roll=-1.571, pitch=1.571, yaw=-1.571
    )
    poses = [home_pose, left_pose, right_pose, home_pose]

    print("Start")

    print("Connect to NiryoRobot")
    robot = NiryoRobot("10.10.10.10")
    #robot.arm.reset_calibration()
    if 0:
        robot.arm.request_new_calibration()
    print("Calibrate NiryoNED if necessary")
    robot.arm.calibrate_auto()
    robot.arm.set_learning_mode(False)
    robot.tool.enable_tcp(False)

    print("Close gripper")
    robot.tool.open_gripper(speed=300)

    print("Move NiryoNED along poses")
    for pose in poses:
        robot.arm.move_pose(pose)

    print("Close gripper")
    robot.tool.close_gripper(speed=300)
    time.sleep(2)
    print("Open gripper")


    print("Move NiryoNED 0.2 m down")
    new_pose = home_pose.copy_with_offsets(z_offset=-0.2)
    robot.arm.move_pose(new_pose)
    time.sleep(2)
    print("Move NiryoNED to home position")
    robot.arm.move_pose(home_pose)
    robot.end()

    print("Ready")

if __name__ == "__main__":
    main()