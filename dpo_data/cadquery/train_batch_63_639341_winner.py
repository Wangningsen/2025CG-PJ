import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-23,0))
r=w0.workplane(offset=-77/2).moveTo(-61,-40).cylinder(77,2).union(w0.workplane(offset=123/2).moveTo(12.5,9).box(101,66,123))