import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,81))
r=w0.workplane(offset=-162/2).box(64,200,162)