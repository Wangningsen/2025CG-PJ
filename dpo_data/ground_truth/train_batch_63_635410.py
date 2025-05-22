import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-70))
r=w0.workplane(offset=141/2).cylinder(141,100)