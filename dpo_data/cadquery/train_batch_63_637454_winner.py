import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-42,0))
r=w0.sketch().segment((-100,-34),(-4,-34)).segment((-4,-7)).segment((25,-7)).arc((81,-68),(44,7)).segment((44,75)).segment((-11,75)).segment((-11,22)).segment((-100,22)).close().assemble().finalize().extrude(84)