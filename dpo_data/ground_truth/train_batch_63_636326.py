import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-43))
w1=cq.Workplane('ZX',origin=(0,46,0))
r=w0.workplane(offset=-57/2).moveTo(0,-43).box(34,6,57).union(w1.workplane(offset=-70/2).moveTo(77,-6).box(46,20,70))