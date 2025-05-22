import cadquery as cq
w0=cq.Workplane('YZ',origin=(-73,0,0))
r=w0.workplane(offset=146/2).box(200,106,146)