import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-2,0))
r=w0.sketch().arc((-100,3),(0,-3),(56,-92)).arc((51,78),(-100,3)).assemble().finalize().extrude(4)