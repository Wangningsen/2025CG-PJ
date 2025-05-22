import cadquery as cq
w0=cq.Workplane('YZ',origin=(98,0,0))
r=w0.workplane(offset=-196/2).box(200,104,196)