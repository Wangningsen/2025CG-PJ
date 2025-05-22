import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-52))
r=w0.workplane(offset=104/2).box(196,200,104)