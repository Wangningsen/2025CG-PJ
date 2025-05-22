import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-23,0))
w1=cq.Workplane('ZX',origin=(0,-29,0))
r=w0.sketch().arc((26,-42),(-33,9),(36,37)).arc((48,42),(63,53)).arc((-62,14),(39,-70)).arc((29,-54),(26,-42)).assemble().finalize().extrude(-77).union(w1.sketch().segment((-53,-10),(4,-10)).arc((4,0),(5,10)).segment((-53,10)).close().assemble().finalize().extrude(129))