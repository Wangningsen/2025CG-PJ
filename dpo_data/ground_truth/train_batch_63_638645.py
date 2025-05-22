import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-8,0))
r=w0.workplane(offset=-92/2).box(38,76,92).union(w0.workplane(offset=108/2).cylinder(108,63))