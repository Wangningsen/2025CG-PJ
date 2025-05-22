import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,28))
w1=cq.Workplane('XY',origin=(0,0,-35))
r=w0.workplane(offset=7/2).moveTo(0,-11).cylinder(7,89).union(w1.workplane(offset=16/2).moveTo(-12.5,17.5).box(135,165,16))