import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,36,0))
r=w0.sketch().segment((76,-54),(94,-54)).segment((94,-1)).arc((100,10),(94,23)).segment((94,76)).segment((76,76)).segment((76,23)).arc((70,10),(76,-1)).close().assemble().finalize().extrude(-72).union(w0.workplane(offset=-26/2).moveTo(-11,0).cylinder(26,91))