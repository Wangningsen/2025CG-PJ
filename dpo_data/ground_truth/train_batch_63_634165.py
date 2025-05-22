import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-26,0))
w1=cq.Workplane('ZX',origin=(0,-86,0))
r=w0.workplane(offset=111/2).moveTo(-26,6).cylinder(111,4).union(w1.sketch().arc((-3,-64),(96,-40),(37,44)).arc((-95,32),(-3,-64)).assemble().finalize().extrude(105))