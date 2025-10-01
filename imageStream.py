import cv2
import numpy as np
import time

try:
    # NOTE: The user's provided code uses this import. This is correct if you have
    # installed the client via pip (`pip install coppeliasim-zmqremoteapi-client`).
    # If you copied the .py file, the import would be `from zmqRemoteApi import RemoteAPIClient`.
    from coppeliasim_zmqremoteapi_client import RemoteAPIClient
    print("ZMQ Remote API client found.")
except ImportError:
    print("Error: Could not import the ZMQ Remote API client. Please install it (`pip install coppeliasim-zmqremoteapi-client`) or place zmqRemoteApi.py in the script's directory.")
    exit()

print('Program started')

# 1. Connect to CoppeliaSim
client = RemoteAPIClient()
sim = client.getObject('sim')

# Get the handle of the vision sensor
# IMPORTANT: Make sure your sensor in CoppeliaSim is named 'visionSensor'
try:
    vision_sensor_handle = sim.getObject('/visionSensor')
    print("Vision sensor handle obtained.")
except Exception as e:
    print(f"Error getting vision sensor handle: {e}")
    print("Please make sure a vision sensor named 'visionSensor' is in the scene.")
    exit()

# It's good practice to check if the simulation is already running
simulation_state = sim.getSimulationState()
if simulation_state == sim.simulation_stopped:
    sim.startSimulation()
    print("Simulation started.")
else:
    print("Simulation is already running.")


# --- MODIFICATION IS HERE ---
# The original loop `while (t := sim.getSimulationTime()) < 10:` is replaced
# with `while True:` to run indefinitely.
print("Streaming video... Press 'q' on the OpenCV window to stop.")

# Main loop
while True: # Run indefinitely until 'q' is pressed
    # 2. Get the image from the vision sensor
    img, res = sim.getVisionSensorImg(vision_sensor_handle)

    if img:
        # 3. Convert the raw image data to a NumPy array
        img_np = np.frombuffer(img, dtype=np.uint8).reshape(res[1], res[0], 3)

        # 4. Correct the image orientation and color format
        img_np = cv2.flip(img_np, 0) # Flip vertically
        img_np = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR) # Convert RGB to BGR for OpenCV

        # 5. Display the image using OpenCV
        cv2.imshow('CoppeliaSim Vision Sensor', img_np)

        # Allow the window to update and check for a key press
        # If 'q' is pressed, break the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("'q' pressed, stopping.")
            break
    else:
        # Check if the simulation is still running before printing an error
        if sim.getSimulationState() != sim.simulation_stopped:
            print("Failed to get image from sensor.")
            time.sleep(0.1)
        else:
            print("Simulation stopped unexpectedly.")
            break

# Stop the simulation
sim.stopSimulation()
print("Simulation stopped.")

# Clean up
cv2.destroyAllWindows()
print('Program ended')