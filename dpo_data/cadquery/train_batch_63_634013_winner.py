import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.workplane(offset=130/2).moveTo(-37,-93).box(114,14,130).union(w0.workplane(offset=200/2).moveTo(88,94).cylinder(200,6))