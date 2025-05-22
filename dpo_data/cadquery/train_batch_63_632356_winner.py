import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((-11,10),(11,-11)).arc((5,6),(-11,10)).assemble().finalize().extrude(200)