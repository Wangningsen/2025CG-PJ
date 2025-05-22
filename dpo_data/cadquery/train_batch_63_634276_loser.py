import cadquery as cq
w0=cq.Workplane('YZ',origin=(57,0,0))
r=w0.workplane(offset=-157/2).moveTo(-1,-1).cylinder(157,10).union(w0.workplane(offset=43/2).box(42,86,43))