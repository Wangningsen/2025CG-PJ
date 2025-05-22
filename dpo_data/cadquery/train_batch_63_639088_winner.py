import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-21,0))
w1=cq.Workplane('XY',origin=(0,0,-21))
r=w0.sketch().arc((-1,-55),(92,-69),(39,9)).arc((-33,11),(-1,-55)).assemble().finalize().extrude(43).union(w1.workplane(offset=-79/2).moveTo(47,0).cylinder(79,46))