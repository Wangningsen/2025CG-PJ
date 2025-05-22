import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,76,0))
r=w0.workplane(offset=-152/2).moveTo(-88,-55).cylinder(152,12).union(w0.sketch().arc((-9,85),(-39,-67),(100,9)).arc((10,11),(-9,85)).assemble().finalize().extrude(-147))