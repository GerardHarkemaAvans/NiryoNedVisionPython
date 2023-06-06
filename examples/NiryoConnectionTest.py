from pyniryo2 import *

robot = NiryoRobot("10.10.10.10")

robot.arm.calibrate_auto()

robot.arm.move_joints(0.2, -0.3, 0.1, 0.0, 0.5, -0.8)

robot.end()