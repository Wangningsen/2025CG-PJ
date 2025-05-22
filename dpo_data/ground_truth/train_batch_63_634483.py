import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,40,0))
r=w0.workplane(offset=-95/2).moveTo(-62,-16).cylinder(95,38).union(w0.workplane(offset=14/2).moveTo(74,28).cylinder(14,26))