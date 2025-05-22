import cadquery as cq
w0=cq.Workplane('YZ',origin=(-25,0,0))
w1=cq.Workplane('YZ',origin=(25,0,0))
r=w0.workplane(offset=50/2).moveTo(0,-24).cylinder(50,76).union(w1.workplane(offset=-50/2).moveTo(-4,36).cylinder(50,64))