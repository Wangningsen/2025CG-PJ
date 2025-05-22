import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-52))
r=w0.sketch().segment((-66,-26),(-59,-26)).arc((37,-90),(19,25)).segment((19,100)).segment((-66,100)).close().assemble().reset().face(w0.sketch().segment((-56,7),(-11,-6)).segment((9,68)).segment((-37,80)).close().assemble(),mode='s').finalize().extrude(103)