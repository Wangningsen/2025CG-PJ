import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,0,0))
w1=cq.Workplane('XY',origin=(0,0,-15))
r=w0.workplane(offset=100/2).moveTo(45,60.5).box(18,15,100).union(w1.workplane(offset=-39/2).moveTo(-17.5,-35).box(101,130,39))