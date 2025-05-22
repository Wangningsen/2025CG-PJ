import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-34))
w1=cq.Workplane('XY',origin=(0,0,-6))
r=w0.workplane(offset=10/2).moveTo(18.5,75).box(163,10,10).union(w1.workplane(offset=40/2).moveTo(-23,-3).cylinder(40,77))