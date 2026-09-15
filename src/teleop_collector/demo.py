import numpy as np
from .models import Frame,RobotState
from .sync import ApproximateSynchronizer
from .archive import write_hdf5
from .quality import validate_trajectory
def main():
    sync=ApproximateSynchronizer(); samples=[]
    for i in range(12):
        t=i/30; img=np.full((16,16,3),i,dtype=np.uint8)
        samples.append(sync.match(Frame(t,img),Frame(t+.003,img),RobotState(t+.001,np.array([0,0,0,0,0,0,1.]),np.ones(14)*i*.01)))
    path="/tmp/synthetic_trajectory.h5"; write_hdf5(path,samples); print(path,validate_trajectory(samples))
if __name__=="__main__":main()
