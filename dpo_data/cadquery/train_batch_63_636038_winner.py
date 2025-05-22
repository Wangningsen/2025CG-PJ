import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,21,0))
w1=cq.Workplane('ZX',origin=(0,-21,0))
r=w0.workplane(offset=-14/2).box(70,118,14).union(w1.workplane(offset=43/2).cylinder(43,100))