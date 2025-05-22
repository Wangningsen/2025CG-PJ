import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,2,0))
r=w0.sketch().arc((-100,3),(1,-4),(56,-92)).arc((50,79),(-100,3)).assemble().finalize().extrude(-4)