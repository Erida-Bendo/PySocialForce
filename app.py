from flask import Flask
import ghhops_server as hs
import simulateHops
import rhino3dm as rg


app = Flask(__name__)
hops = hs.Hops(app)



@hops.component(
    "/simulate",
    name = "Simulate Pedestrian Movement",
    nickname = "Simulate",
    description ="Simulate Pedestrian Movement according to the Social Force Model by Helbing and Molnar",
    inputs=[
        hs.HopsInteger("Step", "No", "Number of Simulation Steps"),
        hs.HopsBoolean("Simulate", "Sim", "Simulate Pedestrian Movement", hs.HopsParamAccess.ITEM, False)
    ],
    outputs=[
        hs.HopsPoint("Positions", "Pos", "Positions of Pedestrians per Step", hs.HopsParamAccess.TREE)
    ]
)

def simulate(steps, toggle):
    positions=[]

    if(toggle==True):
        positions= simulateHops.simulate(steps)
    else:
        positions.append(rg.Point3d(0,0,0))

    return positions

if __name__== "__main__":
    app.run(debug=True)



