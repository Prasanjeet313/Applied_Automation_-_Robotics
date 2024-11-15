import pandas as pd

# Generate synthetic data for particles
num_particles = 500
particle_data = pd.DataFrame({
    'ParticleID': range(1, num_particles + 1),
    'Size': np.random.normal(2.5, 0.5, num_particles),  # Particle size in mm
    'Density': np.random.normal(3.0, 0.4, num_particles),  # Density in g/cm³
    'PositionX': np.random.uniform(-0.5, 0.5, num_particles),
    'PositionY': np.random.uniform(-0.5, 0.5, num_particles),
    'PositionZ': np.random.uniform(0, 1, num_particles),
    'Velocity': np.random.uniform(0, 1, num_particles)
})

# Save data for future use
particle_data.to_csv('synthetic_particle_data.csv', index=False)
print("Synthetic particle data saved to 'synthetic_particle_data.csv'")
