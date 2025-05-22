import cadquery as cq
w0=cq.Workplane('YZ',origin=(-28,0,0))
r=w0.workplane(offset=22/2).moveTo(-36.5,10).box(127,30,22).union(w0.workplane(offset=57/2).moveTo(96,-21).cylinder(57,4))