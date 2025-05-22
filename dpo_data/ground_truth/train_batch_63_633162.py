import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,76,0))
r=w0.workplane(offset=-152/2).moveTo(-88,-55).cylinder(152,12).union(w0.sketch().arc((-9,85),(-36,-69),(100,9)).arc((17,6),(-9,85)).assemble().finalize().extrude(-147))