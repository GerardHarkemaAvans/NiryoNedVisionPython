from pyniryo2 import *

class ONE:
    pass

class NED:
    # NED default poses
    OBSERVATION_POSE = PoseObject(
        x=0.3, y=0.0, z=0.4,
        roll=-1.57, pitch=1.5, yaw=-1.57
    )
    HOME_POSE = PoseObject(
        x=0.25, y=-0.0, z=0.4,
        roll=0, pitch=0, yaw=0
    )
    RESTING_POSE = PoseObject(
        x=0.091, y=-0.004, z=0.187,
        roll=-1.3, pitch=1.5, yaw=-1.25
    )
    # Tool Centre Point offsets
    FINGER_GRIPPER_TCP_OFFSET = PoseObject(
        x=0.085, y=-0.0, z=0.0,
        roll=0.0, pitch=0.0, yaw=0.0
    )
    ADAPTIVE_GRIPPER_TCP_OFFSET = PoseObject(
        x=0.1215, y=-0.0, z=0.0,
        roll=0.0, pitch=0.0, yaw=0.0
    )
    VACUUM_GRIPPER_OFFSET = PoseObject(
        x=0.0, y=-0.0, z=0.0,
        roll=0.0, pitch=0.0, yaw=0.0
    )


class NED2:
    # NED2 poses ar the sam as the NED
    OBSERVATION_POSE = NED.OBSERVATION_POSE
    HOME_POSE = NED.HOME_POSE
    RESTING_POSE = NED.RESTING_POSE
    FINGER_GRIPPER_TCP_OFFSET = NED.FINGER_GRIPPER_TCP_OFFSET
    VACUUM_GRIPPER_OFFSET = NED.VACUUM_GRIPPER_OFFSET
    ADAPTIVE_GRIPPER_TCP_OFFSET = NED.ADAPTIVE_GRIPPER_TCP_OFFSET
