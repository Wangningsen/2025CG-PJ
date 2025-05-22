import cadquery as cq
w0=cq.Workplane('YZ',origin=(54,0,0))
w1=cq.Workplane('ZX',origin=(0,78,0))
r=w0.workplane(offset=-142/2).moveTo(-23,-45).cylinder(142,55).union(w1.workplane(offset=-99/2).moveTo(29,84.5).box(142,7,99))