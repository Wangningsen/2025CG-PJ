import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,38))
r=w0.sketch().segment((-100,-7),(-10,-69)).segment((-10,-70)).segment((-9,-70)).segment((1,-77)).segment((6,-70)).segment((100,-70)).segment((100,77)).segment((-10,77)).segment((-10,54)).segment((-42,77)).close().assemble().finalize().extrude(-76)