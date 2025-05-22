import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,67,0))
r=w0.workplane(offset=-133/2).moveTo(36,-64).cylinder(133,36).union(w0.sketch().arc((-22,80),(-72,47),(-14,32)).arc((25,29),(46,57)).segment((57,57)).segment((57,80)).segment((43,80)).arc((10,100),(-22,80)).assemble().finalize().extrude(-19))