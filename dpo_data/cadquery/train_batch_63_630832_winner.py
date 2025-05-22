import cadquery as cq
w0=cq.Workplane('YZ',origin=(8,0,0))
r=w0.workplane(offset=-16/2).box(200,112,16)