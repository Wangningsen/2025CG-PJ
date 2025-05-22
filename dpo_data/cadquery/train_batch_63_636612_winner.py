import cadquery as cq
w0=cq.Workplane('YZ',origin=(42,0,0))
r=w0.workplane(offset=-84/2).box(200,84,84)