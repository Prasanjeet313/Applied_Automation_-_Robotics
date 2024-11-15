# Function to simulate the rotation of the ball mill
def rotate_ball_mill(rotation_speed=10):
    # Apply rotation to the ball mill
    for _ in range(1000):  # Simulate for 1000 steps
        p.stepSimulation()
        p.resetBaseVelocity(ball_mill_id, angularVelocity=[0, 0, rotation_speed])
    print("Ball mill rotation simulation complete.")

# Run the rotation simulation
rotate_ball_mill(rotation_speed=10)
