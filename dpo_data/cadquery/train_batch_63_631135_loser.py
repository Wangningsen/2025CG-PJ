import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-6))
r=w0.sketch().segment((-100,-19),(-30,-59)).segment((7,6)).arc((99,2),(12,34)).segment((-53,59)).close().assemble().finalize().extrude(12)