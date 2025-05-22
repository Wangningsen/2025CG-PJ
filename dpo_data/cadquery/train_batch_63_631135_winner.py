import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,6))
r=w0.sketch().segment((-100,-19),(-32,-59)).segment((8,4)).arc((99,5),(10,27)).segment((-54,59)).close().assemble().finalize().extrude(-12)