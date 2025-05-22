import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-14))
r=w0.workplane(offset=28/2).box(200,80,28)