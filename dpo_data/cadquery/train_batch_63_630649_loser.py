import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-85,0))
w1=cq.Workplane('ZX',origin=(0,-74,0))
r=w0.sketch().segment((-100,-89),(-95,-89)).segment((-95,-86)).arc((-98,-87),(-100,-86)).close().assemble().finalize().extrude(-2).union(w1.workplane(offset=162/2).moveTo(36,25).cylinder(162,64))