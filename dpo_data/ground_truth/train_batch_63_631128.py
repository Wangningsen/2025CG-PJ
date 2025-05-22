import cadquery as cq
w0=cq.Workplane('YZ',origin=(8,0,0))
w1=cq.Workplane('ZX',origin=(0,62,0))
r=w0.workplane(offset=-78/2).moveTo(-81.5,81.5).box(7,37,78).union(w1.workplane(offset=23/2).moveTo(-94,64).cylinder(23,6))