import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-43))
w1=cq.Workplane('XY',origin=(0,0,-43))
r=w0.workplane(offset=87/2).cylinder(87,100).union(w1.workplane(offset=43/2).box(12,138,43))