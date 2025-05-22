import cadquery as cq
w0=cq.Workplane('YZ',origin=(22,0,0))
r=w0.workplane(offset=-44/2).moveTo(79,43.5).box(42,3,44).union(w0.workplane(offset=-9/2).moveTo(-40,-42).box(120,6,9))