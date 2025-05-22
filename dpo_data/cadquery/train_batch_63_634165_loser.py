import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-86,0))
r=w0.sketch().arc((-3,-63),(96,-40),(38,44)).arc((-95,32),(-3,-63)).assemble().finalize().extrude(105).union(w0.workplane(offset=172/2).moveTo(-25,5).cylinder(172,4))