import cadquery as cq
w0=cq.Workplane('YZ',origin=(-40,0,0))
r=w0.workplane(offset=80/2).box(200,28,80)