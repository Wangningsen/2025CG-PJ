import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-59))
r=w0.sketch().rect(200,166).reset().face(w0.sketch().segment((-47,4),(-45,-15)).segment((47,-4)).segment((45,15)).close().assemble(),mode='s').finalize().extrude(118)