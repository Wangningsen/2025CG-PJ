import cadquery as cq
w0=cq.Workplane('YZ',origin=(-29,0,0))
w1=cq.Workplane('YZ',origin=(-29,0,0))
r=w0.workplane(offset=59/2).moveTo(-29.5,70).box(43,60,59).union(w1.workplane(offset=59/2).moveTo(27,-76).cylinder(59,24))