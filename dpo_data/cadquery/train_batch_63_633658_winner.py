import cadquery as cq
w0=cq.Workplane('YZ',origin=(-43,0,0))
r=w0.workplane(offset=-4/2).moveTo(75,35).box(22,130,4).union(w0.workplane(offset=89/2).moveTo(-77,-36.5).box(18,127,89))