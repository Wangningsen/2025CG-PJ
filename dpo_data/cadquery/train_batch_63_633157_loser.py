import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-29))
r=w0.workplane(offset=58/2).box(4,200,58)