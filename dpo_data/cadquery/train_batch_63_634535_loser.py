import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-11,0))
w1=cq.Workplane('ZX',origin=(0,-66,0))
r=w0.workplane(offset=-89/2).moveTo(0,-11.5).box(88,15,89).union(w1.workplane(offset=166/2).box(66,84,166))