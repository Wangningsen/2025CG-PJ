import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-89,0))
r=w0.sketch().segment((-100,5),(-30,-95)).segment((100,-5)).segment((30,95)).close().assemble().finalize().extrude(178)