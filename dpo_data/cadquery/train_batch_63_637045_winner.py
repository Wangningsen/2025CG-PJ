import cadquery as cq
w0=cq.Workplane('YZ',origin=(63,0,0))
r=w0.workplane(offset=-126/2).moveTo(38,0).box(124,104,126).union(w0.workplane(offset=-13/2).moveTo(-92,-34).cylinder(13,8))