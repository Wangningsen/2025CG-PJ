import cadquery as cq
w0=cq.Workplane('YZ',origin=(-43,0,0))
w1=cq.Workplane('XY',origin=(0,0,-30))
r=w0.workplane(offset=89/2).moveTo(-77,-36.5).box(18,127,89).union(w1.workplane(offset=130/2).moveTo(-44.5,75).box(5,22,130))