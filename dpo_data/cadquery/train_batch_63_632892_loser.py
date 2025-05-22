import cadquery as cq
w0=cq.Workplane('YZ',origin=(71,0,0))
r=w0.workplane(offset=-171/2).box(32,62,171).union(w0.workplane(offset=29/2).cylinder(29,49))