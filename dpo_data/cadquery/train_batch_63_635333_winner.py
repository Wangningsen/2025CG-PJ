import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().rect(92,186).reset().face(w0.sketch().segment((23,-19),(31,-61)).segment((43,-59)).segment((35,-12)).close().assemble(),mode='s').finalize().extrude(200)