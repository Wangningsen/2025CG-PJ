import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,93))
r=w0.sketch().segment((-50,-100),(50,-100)).segment((50,100)).segment((21,100)).arc((-4,94),(-29,100)).segment((-50,100)).close().assemble().finalize().extrude(-186)