import os
import numpy as np
import pysocialforce as psf
from pysocialforce.utils.plot import SceneVisualizer, SimRecording

OUTPUT_DIR = "images/"

if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)


def test_group_crossing():

    initial_state = np.array(
        [
            [0.0, 0.0, 0.5, 0.5, 10.0, 10.0],
            [0.0, 1.0, 0.5, 0.5, 10.0, 10.0],
            [10.0, 0.3, -0.5, 0.5, 0.0, 10.0],
            [11.0, 0.3, -0.5, 0.5, 0.0, 10.0],
            [12.0, 0.3, -0.5, 0.5, 0.0, 10.0],
        ]
    )
    groups = [[0, 1], [2, 3, 4]]
    obs = [[4, 4, 2, 5]]
    rec = SimRecording()
    s = psf.Simulator(initial_state, groups=groups, obstacles=obs, on_step=rec.append_frame)
    s.step(80)
    rec.static_obstacles = s.get_obstacles()

    with SceneVisualizer(rec, OUTPUT_DIR + "group_crossing") as sv:
        sv.animate()
