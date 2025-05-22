import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,32,0))
w1=cq.Workplane('YZ',origin=(34,0,0))
r=w0.sketch().arc((-65,48),(-28,12),(-62,50)).arc((-63,49),(-65,48)).assemble().finalize().extrude(-132).union(w1.workplane(offset=-87/2).moveTo(72,47).cylinder(87,28))