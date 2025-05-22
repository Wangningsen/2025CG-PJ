import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-19,0))
r=w0.sketch().segment((-100,-14),(-58,-14)).arc((0,-59),(58,-14)).segment((100,-14)).segment((100,14)).segment((58,14)).arc((0,59),(-58,14)).segment((-100,14)).close().assemble().finalize().extrude(38)