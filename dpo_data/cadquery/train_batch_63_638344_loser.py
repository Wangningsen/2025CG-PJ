import cadquery as cq
w0=cq.Workplane('YZ',origin=(-48,0,0))
r=w0.workplane(offset=-52/2).cylinder(52,17).union(w0.workplane(offset=148/2).box(128,150,148))