import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-23,0))
w1=cq.Workplane('ZX',origin=(0,-29,0))
r=w0.sketch().arc((25,-43),(-33,9),(40,34)).arc((51,44),(63,53)).arc((-62,15),(38,-70)).arc((30,-57),(25,-43)).assemble().finalize().extrude(-77).union(w1.sketch().segment((-53,-10),(3,-10)).segment((3,1)).segment((4,1)).segment((4,10)).segment((-53,10)).close().assemble().finalize().extrude(129))