import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.workplane(offset=31/2).cylinder(31,20).union(w0.workplane(offset=200/2).cylinder(200,44))