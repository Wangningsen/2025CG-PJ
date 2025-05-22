import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-28))
r=w0.workplane(offset=57/2).box(4,200,57)