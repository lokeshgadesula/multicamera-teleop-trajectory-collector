import numpy as np
from teleop_collector.models import Frame,RobotState
from teleop_collector.sync import ApproximateSynchronizer
from teleop_collector.quality import validate_trajectory
def s(t,j=0):
    x=np.zeros((8,8,3),dtype=np.uint8)
    return ApproximateSynchronizer().match(Frame(t,x),Frame(t+.001,x),RobotState(t+.002,np.array([0,0,0,0,0,0,1.]),np.ones(14)*j))
def test_good(): assert validate_trajectory([s(i/30,i*.01) for i in range(10)]).valid
def test_anomaly(): assert validate_trajectory([s(0),s(1/30),s(2/30,2)]).motion_anomalies==[2]
