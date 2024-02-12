from pymavlink import mavutil
import time

# Connect to the vehicle
master = mavutil.mavlink_connection('udpin:0.0.0.0:14542') # Change as per your connection
master.wait_heartbeat()

# Function to change flight mode
def set_mode_px5(mode):
    if mode in mode_mapping:
        # Extract main mode (first element of the tuple) and convert to float
        mode_id = float(mode_mapping[mode][0])

        master.mav.command_long_send(
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_CMD_DO_SET_MODE,
            0,  # Confirmation
            mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
            mode_id,  # Passed as float
            0.0, 0.0, 0.0, 0.0, 0.0)  # Ensure all other params are floats
        print(f"Mode changed to {mode}")
    else:
        print("Unsupported mode.")
'''
def set_mode_px4(mode):
    if mode in mode_mapping:
        mode_id = mode_mapping[mode]
        master.mav.command_long_send(
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_CMD_DO_SET_MODE,
            0,  # Confirmation
            mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
            mode_id,
            0, 0, 0, 0, 0)
        print(f"Mode changed to {mode}")
    else:
        print("Unsupported mode.")

def set_mode(mode):
    if mode in mode_mapping:
        mode_id = mode_mapping[mode]
        master.mav.set_mode_send(
            master.target_system,
            mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
            mode_id)
        print(f"Mode changed to {mode}")
    else:
        print("Unsupported mode.")

 '''

# Get mode mapping
mode_mapping = master.mode_mapping()

# List all modes
print("Supported Modes:")
for mode in mode_mapping:
    print(f"{mode}")

# User input to select mode
try:
    mode_input = int(input("Enter the number corresponding to the mode you want to set: "))
    selected_mode = list(mode_mapping.keys())[mode_input - 1]  # Adjust for 0-indexing
    set_mode_px5(selected_mode)
except (IndexError, ValueError):
    print("Invalid input.")

# Close the connection
    master.close()