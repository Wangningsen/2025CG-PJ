import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,84))
w1=cq.Workplane('ZX',origin=(0,-49,0))
r=w0.workplane(offset=-125/2).moveTo(-74,10).cylinder(125,26).union(w1.sketch().arc((-47,76),(-74,2),(5,9)).arc((29,83),(-47,76)).assemble().finalize().extrude(98))