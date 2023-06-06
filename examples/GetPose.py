from pyniryo2 import *

robot = NiryoRobot("10.10.10.10")

#robot.calibrate_auto()

pose = robot.get_pose()

print(pose)

robot.close_connection()