import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-61))
r=w0.workplane(offset=122/2).cylinder(122,100)