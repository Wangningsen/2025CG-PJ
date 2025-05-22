import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,20))
w1=cq.Workplane('YZ',origin=(-50,0,0))
r=w0.workplane(offset=-58/2).moveTo(79,0).box(42,112,58).union(w1.workplane(offset=-50/2).moveTo(-27,18).cylinder(50,19))