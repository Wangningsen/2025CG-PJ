import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,20,0))
r=w0.sketch().arc((-4,-64),(96,-40),(37,44)).arc((-95,33),(-4,-64)).assemble().finalize().extrude(-105).union(w0.workplane(offset=66/2).moveTo(-26,6).cylinder(66,4))