import cadquery as cq
w0=cq.Workplane('YZ',origin=(-12,0,0))
r=w0.workplane(offset=25/2).box(200,138,25)