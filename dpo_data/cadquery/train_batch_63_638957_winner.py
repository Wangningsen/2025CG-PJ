import cadquery as cq
w0=cq.Workplane('YZ',origin=(-58,0,0))
w1=cq.Workplane('YZ',origin=(-52,0,0))
r=w0.workplane(offset=114/2).moveTo(36,2).cylinder(114,65).union(w0.workplane(offset=116/2).moveTo(-41,-9).cylinder(116,57)).union(w1.workplane(offset=61/2).moveTo(58,-3.5).box(60,127,61))