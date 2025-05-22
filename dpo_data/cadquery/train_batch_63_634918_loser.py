import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-99))
r=w0.workplane(offset=198/2).box(24,200,198)