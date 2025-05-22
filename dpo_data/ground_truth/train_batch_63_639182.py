import cadquery as cq
w0=cq.Workplane('YZ',origin=(45,0,0))
r=w0.workplane(offset=-91/2).box(200,58,91)