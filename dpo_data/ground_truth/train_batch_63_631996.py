import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,64))
r=w0.workplane(offset=-129/2).box(200,158,129)