import cadquery as cq
w0=cq.Workplane('YZ',origin=(-29,0,0))
r=w0.workplane(offset=23/2).moveTo(-36.5,10).box(127,30,23).union(w0.workplane(offset=58/2).moveTo(96,-21).cylinder(58,4))