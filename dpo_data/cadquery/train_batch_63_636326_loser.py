import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-24,0))
w1=cq.Workplane('ZX',origin=(0,-40,0))
r=w0.workplane(offset=70/2).moveTo(77,-6).box(46,20,70).union(w1.workplane(offset=-6/2).moveTo(-71.5,0).box(57,34,6))