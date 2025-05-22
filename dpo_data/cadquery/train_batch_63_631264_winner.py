import cadquery as cq
w0=cq.Workplane('YZ',origin=(-4,0,0))
r=w0.workplane(offset=-96/2).cylinder(96,14).union(w0.workplane(offset=104/2).box(22,40,104))