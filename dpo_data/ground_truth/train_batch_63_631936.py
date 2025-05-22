import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-9))
r=w0.workplane(offset=18/2).box(76,200,18)