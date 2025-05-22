import cadquery as cq
w0=cq.Workplane('YZ',origin=(-29,0,0))
r=w0.workplane(offset=59/2).box(122,200,59)