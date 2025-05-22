import cadquery as cq
w0=cq.Workplane('YZ',origin=(-53,0,0))
r=w0.workplane(offset=106/2).box(200,54,106)