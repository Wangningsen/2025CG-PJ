import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,30))
w1=cq.Workplane('ZX',origin=(0,93,0))
r=w0.workplane(offset=-72/2).moveTo(11,35).cylinder(72,65).union(w1.sketch().segment((-14,-76),(42,-76)).segment((42,28)).arc((14,22),(-14,28)).close().assemble().finalize().extrude(-193))