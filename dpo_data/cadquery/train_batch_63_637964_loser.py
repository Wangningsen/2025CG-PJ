import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-13))
w1=cq.Workplane('XY',origin=(0,0,-83))
r=w0.workplane(offset=89/2).moveTo(35.5,-93).box(63,14,89).union(w1.workplane(offset=167/2).moveTo(-6,39).cylinder(167,61))