import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-41))
w1=cq.Workplane('ZX',origin=(0,-49,0))
r=w0.workplane(offset=125/2).moveTo(-74,10).cylinder(125,26).union(w1.sketch().arc((-48,76),(-74,2),(5,10)).arc((28,84),(-48,76)).assemble().finalize().extrude(97))