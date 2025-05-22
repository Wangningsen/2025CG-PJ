import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,12,0))
r=w0.workplane(offset=-96/2).moveTo(-3,-20).cylinder(96,35).union(w0.sketch().segment((-100,-68),(3,-68)).arc((81,49),(-42,-18)).segment((-100,-18)).close().assemble().finalize().extrude(45)).union(w0.workplane(offset=71/2).moveTo(-3.5,-20).box(31,62,71))