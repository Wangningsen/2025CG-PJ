import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-43))
r=w0.workplane(offset=86/2).cylinder(86,100)