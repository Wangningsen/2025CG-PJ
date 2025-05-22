import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,38))
r=w0.sketch().segment((-100,-7),(-10,-69)).segment((-10,-70)).segment((-9,-70)).segment((-2,-77)).segment((3,-70)).segment((100,-70)).segment((100,77)).segment((-10,77)).segment((-10,55)).segment((-41,77)).close().assemble().finalize().extrude(-76)