import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,92))
r=w0.sketch().segment((-100,-14),(-25,-98)).segment((100,14)).segment((25,98)).segment((-5,71)).segment((-5,59)).segment((-18,59)).close().assemble().finalize().extrude(-184)