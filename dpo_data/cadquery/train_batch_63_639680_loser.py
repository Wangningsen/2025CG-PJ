import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,23,0))
r=w0.sketch().segment((-100,-14),(-20,-14)).arc((0,-24),(20,-14)).segment((100,-14)).segment((100,14)).segment((20,14)).arc((0,24),(-20,14)).segment((-100,14)).close().assemble().finalize().extrude(-46)