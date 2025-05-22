import cadquery as cq
w0=cq.Workplane('YZ',origin=(-55,0,0))
r=w0.workplane(offset=106/2).moveTo(-64,-55).cylinder(106,36).union(w0.workplane(offset=110/2).moveTo(56,47).cylinder(110,44))