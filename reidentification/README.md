# Person Re-Identification

Real-time face-based person re-identification using SFace model.

## How to Run

**Option 1: Double-click the batch file**
```
run_reid.bat
```

**Option 2: Command line**
```powershell
python realtime_reid_sface.py
```

## How to Use

1. Press `1-9` to register different people (show face to camera)
2. Press `r` to toggle Re-ID mode ON
3. The system will identify who is in front of the camera

## Controls

- `1-9` - Register person
- `r` - Toggle Re-ID mode
- `d` - Toggle debug (show all similarity scores)
- `c` - Clear gallery
- `+/-` - Adjust threshold
- `q` - Quit

## Features

- Face-based recognition using OpenCV SFace model
- Real-time person identification
- Adjustable similarity threshold
- Debug mode to see all scores

## Files

- `realtime_reid_sface.py` - Main demo with SFace model
- `realtime_reid_fast.py` - Fast version with simple CNN
- `realtime_reid_v2.py` - ViT-based version
- `realtime_reid_osnet.py` - OSNet architecture version
- `camera_test.py` - Camera testing utility
