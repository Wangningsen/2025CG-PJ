import cadquery as cq
w0=cq.Workplane('YZ',origin=(-72,0,0))
r=w0.workplane(offset=35/2).moveTo(-29,-68).cylinder(35,32).union(w0.workplane(offset=144/2).moveTo(43,82).cylinder(144,18))