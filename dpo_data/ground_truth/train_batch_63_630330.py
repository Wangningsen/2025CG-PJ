import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,36))
r=w0.workplane(offset=-73/2).cylinder(73,100)