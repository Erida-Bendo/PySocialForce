import pysocialforce as pysf
import rhino3dm as rg

def simulate(steps):
    map_def = pysf.load_map("./maps/GHMap.json")
    simulator = pysf.Simulator_v2(map_def)
    """
    #Assign force factors - overwrites the config.py file
    #general
    simulator.config.scene_config.max_speed_multiplier =2
    simulator.config.social_force_config.factor = 6
    simulator.config.social_force_config.activation_threshold = 50
    simulator.config.social_force_config.lambda_importance = 4
    simulator.config.scene_config.tau = 1 #speeds the simulation

    #obstacles
    simulator.config.obstacle_force_config.factor=20
    simulator.config.obstacle_force_config.threshold=-0.2

    #groups
    simulator.config.group_coherence_force_config.factor = 1
    simulator.config.group_gaze_force_config.factor = 0.1

    #goal
    simulator.config.desired_force_config.factor = 3
    """
    positions =[]

    for step in range(steps):
        simulator.step()
        for point in simulator.states.ped_positions:
            pt= rg.Point3d(point[0], 200-point[1], 0)
            positions.append(pt)

    return positions


