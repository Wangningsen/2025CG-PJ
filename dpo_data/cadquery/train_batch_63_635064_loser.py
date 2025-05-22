import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,6,0))
r=w0.workplane(offset=-67/2).moveTo(-41,11).cylinder(67,59).union(w0.workplane(offset=-58/2).moveTo(80,-50).cylinder(58,20)).union(w0.workplane(offset=55/2).moveTo(-41,11).cylinder(55,53))