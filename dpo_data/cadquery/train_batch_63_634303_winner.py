import cadquery as cq
w0=cq.Workplane('YZ',origin=(-68,0,0))
r=w0.workplane(offset=62/2).moveTo(95,-82).cylinder(62,5).union(w0.workplane(offset=136/2).moveTo(-48.5,67).box(103,40,136))