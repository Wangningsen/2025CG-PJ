import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-29))
r=w0.sketch().segment((-100,-12),(-37,-12)).arc((0,-39),(37,-12)).segment((100,-12)).segment((100,12)).segment((37,12)).arc((0,39),(-37,12)).segment((-100,12)).close().assemble().finalize().extrude(58)