import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,41,0))
w1=cq.Workplane('ZX',origin=(0,38,0))
r=w0.workplane(offset=-82/2).moveTo(44,-97.5).box(8,5,82).union(w1.workplane(offset=-67/2).moveTo(-1.5,54.5).box(93,91,67))