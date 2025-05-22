import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,93,0))
w1=cq.Workplane('XY',origin=(0,0,30))
r=w0.sketch().segment((-14,-76),(42,-76)).segment((42,28)).arc((19,22),(-5,26)).segment((-5,22)).segment((-14,22)).close().assemble().finalize().extrude(-193).union(w1.workplane(offset=-72/2).moveTo(11,35).cylinder(72,65))