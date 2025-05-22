import cadquery as cq
w0=cq.Workplane('YZ',origin=(-43,0,0))
r=w0.workplane(offset=85/2).box(200,16,85)