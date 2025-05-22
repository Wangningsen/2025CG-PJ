import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,42,0))
r=w0.workplane(offset=-142/2).cylinder(142,58).union(w0.workplane(offset=58/2).moveTo(-0.5,-0.5).box(29,39,58))