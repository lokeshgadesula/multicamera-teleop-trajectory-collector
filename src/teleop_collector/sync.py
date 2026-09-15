from .models import Frame,RobotState,SyncedSample
class ApproximateSynchronizer:
    def __init__(self,tolerance_s=.02): self.tolerance_s=tolerance_s
    def match(self,a:Frame,b:Frame,r:RobotState):
        ts=[a.timestamp,b.timestamp,r.timestamp]
        if max(ts)-min(ts)>self.tolerance_s: raise ValueError("sync tolerance exceeded")
        return SyncedSample(sum(ts)/3,a,b,r)
