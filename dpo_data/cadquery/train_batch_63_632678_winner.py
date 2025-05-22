import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-21,0))
w1=cq.Workplane('ZX',origin=(0,-74,0))
r=w0.workplane(offset=-30/2).moveTo(15,-32).box(170,114,30).union(w1.workplane(offset=149/2).moveTo(-63,52).cylinder(149,37))