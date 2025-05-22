import cadquery as cq
w0=cq.Workplane('YZ',origin=(-9,0,0))
r=w0.workplane(offset=-30/2).moveTo(11,-78).cylinder(30,22).union(w0.workplane(offset=48/2).moveTo(-14,81).cylinder(48,19))