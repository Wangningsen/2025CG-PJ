import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,21))
r=w0.workplane(offset=-42/2).box(200,158,42)