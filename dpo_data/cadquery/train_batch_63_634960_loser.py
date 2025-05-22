import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,59))
r=w0.sketch().rect(200,166).reset().face(w0.sketch().segment((-47,-15),(47,-4)).segment((46,15)).segment((-46,4)).close().assemble(),mode='s').finalize().extrude(-118)