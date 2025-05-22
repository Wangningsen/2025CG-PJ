import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,8,0))
w1=cq.Workplane('XY',origin=(0,0,7))
r=w0.workplane(offset=-20/2).moveTo(29,-37).box(80,104,20).union(w0.workplane(offset=92/2).moveTo(-58.5,17.5).box(5,27,92)).union(w1.workplane(offset=-76/2).moveTo(35.5,-63).box(107,74,76))