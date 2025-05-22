import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-86,0))
w1=cq.Workplane('ZX',origin=(0,18,0))
r=w0.sketch().segment((94,64),(94,65)).segment((97,65)).segment((97,64)).arc((95,74),(94,64)).assemble().finalize().extrude(104).union(w1.sketch().push([(-40.5,-3)]).rect(119,142).reset().face(w1.sketch().arc((-77,-6),(-72,-20),(-67,-6)).segment((-67,20)).segment((-77,20)).close().assemble(),mode='s').reset().face(w1.sketch().segment((-15,-27),(-6,-27)).segment((-6,21)).segment((-15,21)).segment((-15,-10)).arc((-12,-18),(-15,-26)).close().assemble(),mode='s').finalize().extrude(68))