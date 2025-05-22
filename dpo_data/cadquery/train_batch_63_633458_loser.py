import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-15,0))
r=w0.workplane(offset=-61/2).moveTo(-30,68).cylinder(61,32).union(w0.workplane(offset=91/2).moveTo(43,-81).cylinder(91,19))