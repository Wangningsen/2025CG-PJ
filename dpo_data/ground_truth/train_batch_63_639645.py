import cadquery as cq
w0=cq.Workplane('YZ',origin=(27,0,0))
w1=cq.Workplane('YZ',origin=(49,0,0))
r=w0.workplane(offset=-119/2).box(114,200,119).union(w1.workplane(offset=43/2).cylinder(43,20))