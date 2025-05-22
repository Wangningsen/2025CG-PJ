import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().arc((-64,-40),(-11,30),(66,-19)).arc((-12,39),(-64,-40)).assemble().finalize().extrude(-200)