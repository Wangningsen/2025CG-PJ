import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-71))
r=w0.workplane(offset=143/2).cylinder(143,100)