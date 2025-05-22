import cadquery as cq
w0=cq.Workplane('YZ',origin=(53,0,0))
r=w0.workplane(offset=-107/2).moveTo(-98,31).cylinder(107,2).union(w0.workplane(offset=-58/2).moveTo(39,0).cylinder(58,61))