"""
# Example 03: simulate with visual rendering
"""

import pysocialforce as pysf


map_def = pysf.load_map("../maps/GHMap.json")
display = pysf.SimulationView(obstacles=map_def.obstacles, scaling=4)
render_step = lambda t, s: display.render(pysf.to_visualizable_state(t, s))
simulator = pysf.Simulator_v2(map_def, on_step=render_step)
"""
#Assign force factors - overwrites the config.py file
#general
#simulator.config.scene_config.agent_radius = 1000
#simulator.config.scene_config.max_speed_multiplier = 5
#increases repulsion between pedestrians
#simulator.config.social_force_config.gamma = 0.35
simulator.config.social_force_config.factor = 6
simulator.config.social_force_config.activation_threshold = 50
simulator.config.social_force_config.lambda_importance = 4
#simulator.config.social_force_config.n_prime=5

simulator.config.scene_config.tau = 1 #speeds the simulation
#simulator.config.scene_config.dt_secs = 2


#obstacles
simulator.config.obstacle_force_config.factor=20
simulator.config.obstacle_force_config.threshold=-0.2

#groups
simulator.config.group_coherence_force_config.factor = 1
simulator.config.group_gaze_force_config.factor = 0.1
#simulator.config.group_repulsive_force_config.factor = 50
#goal
simulator.config.desired_force_config.factor = 3
"""

display.show()
for step in range(10_000):
    simulator.step()
display.exit()
