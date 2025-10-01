
# CoppeliaSim Vision Sensor Image Stream using OpenCV and ZMQ Remote API
This program is designed to stream images from a CoppeliaSim vision sensor using OpenCV for image processing and the ZMQ Remote API for communication with CoppeliaSim.

## Installation Requirements:

Install CoppeliaSim ZMQ Remote API Client:
```sh
pip install coppeliasim-zmqremoteapi-client
```

Install OpenCV:
```sh
pip install opencv-python
```

Install NumPy:
```sh
pip install numpy
```

## Usage:
1. Ensure that CoppeliaSim is running and that the ZMQ Remote API server is enabled.
2. Run the script:
```sh
python imageStream.py
```

3. The script will connect to CoppeliaSim, retrieve images from the specified vision sensor, and display them in a window using OpenCV.
4. Press any key to exit the image display window.
5. The script will clean up and close the connection to CoppeliaSim upon exit.
6. Make sure to adjust the `visionSensorName` variable in the script to match the name of your vision sensor in CoppeliaSim.
