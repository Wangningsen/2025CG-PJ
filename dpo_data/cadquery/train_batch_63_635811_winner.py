import cadquery as cq
w0=cq.Workplane('YZ',origin=(-29,0,0))
r=w0.workplane(offset=8/2).moveTo(27,34).box(146,44,8).union(w0.workplane(offset=58/2).moveTo(-69,-25).cylinder(58,31))