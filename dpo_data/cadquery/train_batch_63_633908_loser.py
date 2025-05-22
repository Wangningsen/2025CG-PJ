import cadquery as cq
w0=cq.Workplane('YZ',origin=(23,0,0))
r=w0.workplane(offset=-57/2).moveTo(-26,-45).box(148,68,57).union(w0.workplane(offset=11/2).moveTo(65,44).cylinder(11,35))