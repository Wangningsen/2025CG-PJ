import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-74,0))
w1=cq.Workplane('ZX',origin=(0,-51,0))
r=w0.workplane(offset=148/2).moveTo(-63,52).cylinder(148,37).union(w1.workplane(offset=29/2).moveTo(15,-32).box(170,114,29))