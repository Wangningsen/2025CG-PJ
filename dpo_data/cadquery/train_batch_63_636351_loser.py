import cadquery as cq
w0=cq.Workplane('YZ',origin=(88,0,0))
w1=cq.Workplane('YZ',origin=(54,0,0))
r=w0.workplane(offset=-7/2).moveTo(28.5,29).box(99,142,7).union(w1.workplane(offset=-142/2).moveTo(-23,-45).cylinder(142,55))