import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-19,0))
r=w0.sketch().segment((-100,-26),(-92,-26)).arc((0,-96),(92,-26)).segment((100,-26)).segment((100,26)).segment((92,26)).arc((0,96),(-92,26)).segment((-100,26)).close().assemble().finalize().extrude(38)