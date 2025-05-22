import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-50))
r=w0.workplane(offset=100/2).box(200,160,100)