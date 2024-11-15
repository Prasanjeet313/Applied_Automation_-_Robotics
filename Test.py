# Testing the mill's performance by running different rotation speeds and measuring load shapes
for speed in [5, 10, 15]:
    rotate_ball_mill(rotation_speed=speed)
    # Log performance metrics (e.g., power draw, load shape)
    # Adjust DEM-SPH parameters if needed based on observed results
    print(f"Completed rotation speed test at {speed} RPM.")
