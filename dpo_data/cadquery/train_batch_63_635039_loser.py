import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,56,0))
r=w0.sketch().segment((-97,-7),(-22,-100)).segment((87,-12)).segment((76,2)).arc((78,87),(-7,65)).close().assemble().finalize().extrude(-111)