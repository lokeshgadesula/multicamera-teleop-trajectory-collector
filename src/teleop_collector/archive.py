import h5py, numpy as np
def write_hdf5(path,samples):
    if not samples: raise ValueError("empty trajectory")
    with h5py.File(path,"w") as f:
        f.create_dataset("timestamp",data=[s.timestamp for s in samples])
        f.create_dataset("camera_a/rgb",data=np.stack([s.camera_a.rgb for s in samples]),compression="gzip")
        f.create_dataset("camera_b/rgb",data=np.stack([s.camera_b.rgb for s in samples]),compression="gzip")
        f.create_dataset("robot/pose_xyz_quat",data=np.stack([s.robot.pose_xyz_quat for s in samples]))
        f.create_dataset("robot/joints",data=np.stack([s.robot.joints for s in samples]))
