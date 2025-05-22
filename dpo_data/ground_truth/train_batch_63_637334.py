import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-33,0))
r=w0.sketch().arc((34,94),(-57,-82),(76,65)).arc((36,53),(34,94)).assemble().finalize().extrude(65)