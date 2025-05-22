import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,20))
w1=cq.Workplane('ZX',origin=(0,-50,0))
r=w0.workplane(offset=-59/2).moveTo(-49,-4).cylinder(59,51).union(w1.workplane(offset=105/2).moveTo(1,87).box(76,26,105))