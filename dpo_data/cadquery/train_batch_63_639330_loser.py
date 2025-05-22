import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-31))
w1=cq.Workplane('ZX',origin=(0,57,0))
r=w0.workplane(offset=-69/2).cylinder(69,49).union(w0.workplane(offset=131/2).box(60,92,131)).union(w1.workplane(offset=-114/2).box(96,46,114))