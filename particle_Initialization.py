# Function to add particles to the PyBullet environment
def create_particle(position, size):
    sphere_radius = size / 1000  # Convert mm to meters for PyBullet compatibility
    particle_id = p.createCollisionShape(p.GEOM_SPHERE, radius=sphere_radius)
    visual_shape_id = p.createVisualShape(p.GEOM_SPHERE, radius=sphere_radius, rgbaColor=[1, 0, 0, 1])
    body_id = p.createMultiBody(
        baseMass=0.1,  # Mass of each particle
        baseCollisionShapeIndex=particle_id,
        baseVisualShapeIndex=visual_shape_id,
        basePosition=position
    )
    return body_id

# Initialize particles using the synthetic data
particle_ids = []
for _, particle in particle_data.iterrows():
    position = [particle['PositionX'], particle['PositionY'], particle['PositionZ']]
    size = particle['Size']
    particle_ids.append(create_particle(position, size))
