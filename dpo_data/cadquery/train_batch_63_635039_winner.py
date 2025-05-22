import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,56,0))
r=w0.sketch().segment((-97,-7),(-22,-100)).segment((88,-12)).segment((75,3)).arc((76,89),(-8,65)).close().assemble().finalize().extrude(-111)