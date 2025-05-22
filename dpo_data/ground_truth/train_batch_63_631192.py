import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,29,0))
w1=cq.Workplane('ZX',origin=(0,-22,0))
r=w0.workplane(offset=-58/2).moveTo(-89,-43).cylinder(58,11).union(w1.workplane(offset=30/2).moveTo(48.5,4.5).box(103,99,30))