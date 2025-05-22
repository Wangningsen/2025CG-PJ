import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,95))
r=w0.workplane(offset=-190/2).cylinder(190,100)