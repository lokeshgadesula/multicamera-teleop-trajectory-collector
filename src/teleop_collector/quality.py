from dataclasses import dataclass
import numpy as np
@dataclass
class QualityReport:
    valid:bool; timing_gaps:list[int]; motion_anomalies:list[int]; non_monotonic:list[int]
def validate_trajectory(samples,expected_hz=30,gap_factor=1.8,max_joint_delta=.5):
    if len(samples)<2:return QualityReport(False,[],[],[])
    t=np.array([s.timestamp for s in samples]); dt=np.diff(t)
    non=(np.where(dt<=0)[0]+1).tolist()
    gaps=(np.where(dt>gap_factor/expected_hz)[0]+1).tolist()
    j=np.stack([s.robot.joints for s in samples])
    motion=(np.where(np.max(np.abs(np.diff(j,axis=0)),axis=1)>max_joint_delta)[0]+1).tolist()
    return QualityReport(not(non or gaps or motion),gaps,motion,non)
