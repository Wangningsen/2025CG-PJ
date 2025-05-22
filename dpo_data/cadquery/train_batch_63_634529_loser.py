import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,66))
r=w0.workplane(offset=-132/2).cylinder(132,100)