import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,6,0))
r=w0.workplane(offset=-12/2).moveTo(84,-95).cylinder(12,5).union(w0.workplane(offset=-4/2).moveTo(-81,68).box(16,64,4))