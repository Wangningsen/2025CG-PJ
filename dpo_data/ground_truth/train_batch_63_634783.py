import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-44))
r=w0.workplane(offset=88/2).box(170,200,88)