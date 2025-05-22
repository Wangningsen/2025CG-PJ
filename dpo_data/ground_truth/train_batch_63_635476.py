import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,35))
r=w0.workplane(offset=-71/2).cylinder(71,100)