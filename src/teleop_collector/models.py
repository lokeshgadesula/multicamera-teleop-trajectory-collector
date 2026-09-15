from dataclasses import dataclass
import numpy as np
@dataclass
class Frame:
    timestamp:float
    rgb:np.ndarray
    depth:np.ndarray|None=None
@dataclass
class RobotState:
    timestamp:float
    pose_xyz_quat:np.ndarray
    joints:np.ndarray
@dataclass
class SyncedSample:
    timestamp:float
    camera_a:Frame
    camera_b:Frame
    robot:RobotState
