import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-16,0))
r=w0.workplane(offset=-61/2).moveTo(-29,68).cylinder(61,32).union(w0.workplane(offset=92/2).moveTo(43,-81).cylinder(92,19))