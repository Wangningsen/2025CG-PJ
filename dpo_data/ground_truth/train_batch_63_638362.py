import cadquery as cq
w0=cq.Workplane('YZ',origin=(-50,0,0))
r=w0.workplane(offset=101/2).box(200,4,101)