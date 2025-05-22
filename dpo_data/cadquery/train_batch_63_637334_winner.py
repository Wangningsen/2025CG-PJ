import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-32,0))
r=w0.sketch().arc((34,94),(-51,-86),(76,65)).arc((39,51),(34,94)).assemble().finalize().extrude(65)