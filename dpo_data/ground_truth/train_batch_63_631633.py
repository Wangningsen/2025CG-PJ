import cadquery as cq
w0=cq.Workplane('YZ',origin=(6,0,0))
r=w0.workplane(offset=-106/2).moveTo(7,31).cylinder(106,67).union(w0.workplane(offset=94/2).moveTo(-62.5,-50).box(23,96,94))