import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-48,0))
r=w0.workplane(offset=-19/2).cylinder(19,28).union(w0.workplane(offset=115/2).box(150,200,115))