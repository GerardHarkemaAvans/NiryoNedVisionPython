from pyniryo2 import *
import json

from cv2 import *



class Workspace:

    def __init__(self):

        self.UpperRightPose = PoseObject(x=-1000.0, y=-1000.0, z=0.1, roll=0, pitch=0, yaw=0)
        self.UpperLeftPose = PoseObject(x=1000.0, y=-1000.0, z=0.1, roll=0, pitch=0, yaw=0)
        self.LowerRightPose = PoseObject(x=-1000.0, y=1000.0, z=0.1, roll=0, pitch=0, yaw=0)
        self.LowerLeftPose = PoseObject(x=1000.0, y=1000.0, z=0.1, roll=0, pitch=0, yaw=0)

    def set(self, _upper_right_pose, _upper_left_pose, _lower_right_pose, _lower_left_pose):
        self.LowerRightPose = _lower_right_pose
        self.LowerLeftPose = _lower_left_pose
        self.UpperRightPose = _upper_right_pose
        self.UpperLeftPose = _upper_left_pose

    def get(self):
        return self.UpperRightPose, self.UpperLeftPose, self.LowerRightPose, self.LowerLeftPose

    def to_json(self):
        poses_json = {}

        poses_json["UpperRightPose"] = {}
        poses_json["UpperRightPose"]['x'] = self.UpperRightPose.x
        poses_json["UpperRightPose"]['y'] = self.UpperRightPose.y
        poses_json["UpperRightPose"]['z'] = self.UpperRightPose.z

        poses_json["UpperLeftPose"] = {}
        poses_json["UpperLeftPose"]['x'] = self.UpperLeftPose.x
        poses_json["UpperLeftPose"]['y'] = self.UpperLeftPose.y
        poses_json["UpperLeftPose"]['z'] = self.UpperLeftPose.z

        poses_json["LowerRightPose"] = {}
        poses_json["LowerRightPose"]['x'] = self.LowerRightPose.x
        poses_json["LowerRightPose"]['y'] = self.LowerRightPose.y
        poses_json["LowerRightPose"]['z'] = self.LowerRightPose.z

        poses_json["LowerLeftPose"] = {}
        poses_json["LowerLeftPose"]['x'] = self.LowerLeftPose.x
        poses_json["LowerLeftPose"]['y'] = self.LowerLeftPose.y
        poses_json["LowerLeftPose"]['z'] = self.LowerLeftPose.z

        json_string = json.dumps(poses_json)
        return json_string

    def from_json(self, json_string):
        poses_json = json.loads(json_string)
        try:
            self.UpperRightPose.x = poses_json["UpperRightPose"]['x']
            self.UpperRightPose.y = poses_json["UpperRightPose"]['y']
            self.UpperRightPose.z = poses_json["UpperRightPose"]['z']

            self.UpperLeftPose.x = poses_json["UpperLeftPose"]['x']
            self.UpperLeftPose.y = poses_json["UpperLeftPose"]['y']
            self.UpperLeftPose.z = poses_json["UpperLeftPose"]['z']

            self.LowerRightPose.x = poses_json["LowerRightPose"]['x']
            self.LowerRightPose.y = poses_json["LowerRightPose"]['y']
            self.LowerRightPose.z = poses_json["LowerRightPose"]['z']

            self.LowerLeftPose.x = poses_json["LowerLeftPose"]['x']
            self.LowerLeftPose.y = poses_json["LowerLeftPose"]['y']
            self.LowerLeftPose.z = poses_json["LowerLeftPose"]['z']
        except KeyError as ke:
            print('Key Not Found in Poses Dictionary:', ke)
            return False
        return True

    def get_pose(self, x_rel, y_rel, yaw_rel, yaw_center=None):
        # simple way, better to implement matrixes

        pose = PoseObject(x=-1000.0, y=-1000.0, z=0.1, roll=0, pitch=0, yaw=0)

        # x-direction
        delta_x_ws = self.LowerLeftPose.x - self.UpperRightPose.x
        rel_x_ws = delta_x_ws * x_rel
        abs_x_ws = self.UpperRightPose.x + rel_x_ws
        pose.x = abs_x_ws

        # y-direction
        delta_y_ws = self.LowerLeftPose.y - self.UpperRightPose.y
        rel_y_ws = delta_y_ws * y_rel
        abs_y_ws = self.UpperRightPose.x + rel_y_ws
        pose.y = abs_y_ws

        # x-direction
        abs_z_ws = (self.UpperRightPose.z + self.UpperLeftPose.z + self.LowerRightPose.z + self.LowerLeftPose.z) / 4
        pose.z = abs_z_ws

        # yaw-orientation
        pose.yaw = yaw_rel

        return pose

