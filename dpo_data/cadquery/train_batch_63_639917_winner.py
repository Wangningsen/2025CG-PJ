import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,78,0))
r=w0.workplane(offset=-156/2).moveTo(88,80).box(10,40,156).union(w0.workplane(offset=-94/2).moveTo(-75,-95).box(36,10,94))