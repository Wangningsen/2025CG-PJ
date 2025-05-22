import cadquery as cq
w0=cq.Workplane('YZ',origin=(-77,0,0))
r=w0.workplane(offset=154/2).box(200,146,154)