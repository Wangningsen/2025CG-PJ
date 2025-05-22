import cadquery as cq
w0=cq.Workplane('YZ',origin=(75,0,0))
r=w0.workplane(offset=-150/2).box(114,200,150)