import cadquery as cq
w0=cq.Workplane('YZ',origin=(-8,0,0))
r=w0.workplane(offset=-76/2).moveTo(-28,0).cylinder(76,72).union(w0.workplane(offset=92/2).moveTo(93,-30).cylinder(92,7))