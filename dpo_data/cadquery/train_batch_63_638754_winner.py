import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-64,0))
w1=cq.Workplane('ZX',origin=(0,-45,0))
r=w0.sketch().arc((5,15),(-25,-57),(54,-43)).segment((67,-48)).segment((100,49)).segment((26,75)).close().assemble().finalize().extrude(99).union(w1.sketch().segment((-100,-31),(-78,-31)).arc((-60,-44),(-42,-31)).segment((-21,-31)).segment((-21,-20)).segment((-42,-20)).arc((-60,-7),(-78,-20)).segment((-100,-20)).close().assemble().finalize().extrude(109))