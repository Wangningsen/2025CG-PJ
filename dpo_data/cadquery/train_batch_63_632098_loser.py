import cadquery as cq
w0=cq.Workplane('YZ',origin=(54,0,0))
r=w0.workplane(offset=-108/2).moveTo(-98,31).cylinder(108,2).union(w0.workplane(offset=-59/2).moveTo(39,0).cylinder(59,61))