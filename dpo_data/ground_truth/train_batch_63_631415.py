import cadquery as cq
w0=cq.Workplane('YZ',origin=(84,0,0))
r=w0.workplane(offset=-169/2).moveTo(-18,26.5).box(112,147,169).union(w0.workplane(offset=-56/2).moveTo(26,-52).cylinder(56,48))