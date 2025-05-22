import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,73))
r=w0.workplane(offset=-147/2).box(154,200,147)