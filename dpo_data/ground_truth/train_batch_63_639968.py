import cadquery as cq
w0=cq.Workplane('YZ',origin=(54,0,0))
r=w0.workplane(offset=-108/2).moveTo(-41,11).cylinder(108,59).union(w0.workplane(offset=-73/2).moveTo(5,38).cylinder(73,19)).union(w0.workplane(offset=-3/2).moveTo(61,-31).cylinder(3,39))