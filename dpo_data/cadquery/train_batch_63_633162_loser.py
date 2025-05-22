import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,76,0))
r=w0.workplane(offset=-153/2).moveTo(-88,-55).cylinder(153,12).union(w0.sketch().arc((-9,85),(-46,-61),(100,9)).arc((11,10),(-9,85)).assemble().finalize().extrude(-147))