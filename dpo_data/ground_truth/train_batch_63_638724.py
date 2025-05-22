import cadquery as cq
w0=cq.Workplane('YZ',origin=(26,0,0))
r=w0.workplane(offset=-94/2).moveTo(52,0).box(96,100,94).union(w0.workplane(offset=42/2).moveTo(-60.5,9).box(79,74,42))