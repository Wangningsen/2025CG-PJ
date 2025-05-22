import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-40,0))
r=w0.sketch().segment((-25,-98),(-20,-98)).arc((0,-100),(20,-98)).segment((25,-98)).segment((25,-97)).arc((100,0),(25,97)).segment((25,98)).segment((20,98)).arc((0,100),(-20,98)).segment((-25,98)).segment((-25,97)).arc((-100,0),(-25,-97)).close().assemble().finalize().extrude(81)