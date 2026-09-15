# Multi-Camera Teleoperation Data Ingestion & Trajectory Collector

Hardware-agnostic demonstration recorder and QA layer for robotic-learning datasets.

## Features
- Approximate timestamp synchronization across two cameras and robot state
- RGB/depth-ready frame models
- 6-DoF pose represented as xyz + quaternion and configurable joint commands
- Compressed HDF5 trajectory archives
- Automated checks for timing gaps/frame drops, non-monotonic timestamps, and erratic joint motion
- Synthetic demo and CI tests

```text
camera A --+
camera B --+--> synchronizer --> aligned sample --> HDF5 archive
robot -----+                           |
                                       +--> trajectory QA
```

## Run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
python -m teleop_collector.demo
```
