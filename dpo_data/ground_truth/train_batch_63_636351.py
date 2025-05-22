import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
w1=cq.Workplane('YZ',origin=(54,0,0))
r=w0.workplane(offset=-142/2).moveTo(84.5,28.5).box(7,99,142).union(w1.workplane(offset=-142/2).moveTo(-23,-45).cylinder(142,55))