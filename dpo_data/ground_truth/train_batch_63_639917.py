import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,77,0))
r=w0.workplane(offset=-155/2).moveTo(88,80).box(10,40,155).union(w0.workplane(offset=-93/2).moveTo(-75,-95).box(36,10,93))