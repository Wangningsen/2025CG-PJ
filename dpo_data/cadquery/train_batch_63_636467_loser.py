import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-29,0))
w1=cq.Workplane('ZX',origin=(0,-41,0))
r=w0.workplane(offset=67/2).moveTo(-1.5,54.5).box(93,91,67).union(w1.workplane(offset=82/2).moveTo(43.5,-97.5).box(9,5,82))