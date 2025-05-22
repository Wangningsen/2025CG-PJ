import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-31,0))
r=w0.sketch().segment((-100,-22),(-29,-22)).arc((0,-37),(29,-22)).segment((100,-22)).segment((100,22)).segment((29,22)).arc((0,37),(-29,22)).segment((-100,22)).close().assemble().finalize().extrude(62)