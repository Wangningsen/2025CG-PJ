import cadquery as cq
w0=cq.Workplane('YZ',origin=(-33,0,0))
r=w0.workplane(offset=61/2).cylinder(61,33).union(w0.workplane(offset=67/2).cylinder(67,100))