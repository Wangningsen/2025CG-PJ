import cadquery as cq
w0=cq.Workplane('YZ',origin=(-31,0,0))
r=w0.workplane(offset=62/2).box(142,200,62)