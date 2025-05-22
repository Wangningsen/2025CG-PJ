import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,28,0))
r=w0.workplane(offset=-56/2).box(182,200,56)