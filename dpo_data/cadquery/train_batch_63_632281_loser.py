import cadquery as cq
w0=cq.Workplane('YZ',origin=(34,0,0))
w1=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.workplane(offset=-87/2).moveTo(72,47).cylinder(87,28).union(w1.workplane(offset=132/2).moveTo(-49,27).cylinder(132,26))