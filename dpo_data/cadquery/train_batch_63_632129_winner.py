import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-50,0))
w1=cq.Workplane('XY',origin=(0,0,21))
r=w0.workplane(offset=105/2).moveTo(1,87).box(78,26,105).union(w1.workplane(offset=-60/2).moveTo(-49,-4).cylinder(60,51))