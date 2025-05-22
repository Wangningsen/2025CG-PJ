import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,52))
r=w0.sketch().segment((-67,-20),(-60,-20)).arc((33,-92),(19,25)).segment((19,100)).segment((-67,100)).close().assemble().reset().face(w0.sketch().segment((-58,7),(-12,-6)).segment((10,67)).segment((-37,80)).close().assemble(),mode='s').finalize().extrude(-104)