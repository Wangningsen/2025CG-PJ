import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().arc((-7,1),(-4,0),(-3,-3)).segment((7,-3)).arc((1,3),(-7,1)).assemble().finalize().extrude(-200)