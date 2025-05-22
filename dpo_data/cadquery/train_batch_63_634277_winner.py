import cadquery as cq
w0=cq.Workplane('YZ',origin=(-56,0,0))
r=w0.workplane(offset=107/2).moveTo(-64,-55).cylinder(107,36).union(w0.workplane(offset=111/2).moveTo(56,47).cylinder(111,44))