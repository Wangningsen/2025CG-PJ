import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,50))
r=w0.sketch().arc((-63,-97),(52,-44),(26,81)).arc((14,73),(18,87)).arc((5,94),(-8,100)).arc((-11,-54),(-63,-97)).assemble().finalize().extrude(-100)