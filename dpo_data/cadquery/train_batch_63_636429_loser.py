import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,8,0))
w1=cq.Workplane('ZX',origin=(0,-26,0))
r=w0.workplane(offset=-20/2).moveTo(29,-37).box(80,104,20).union(w0.workplane(offset=92/2).moveTo(-58.5,17.5).box(5,27,92)).union(w1.workplane(offset=-74/2).moveTo(-31,35.5).box(76,107,74))