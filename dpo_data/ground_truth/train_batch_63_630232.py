import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-50,0))
r=w0.sketch().segment((94,-97),(100,-97)).segment((100,-88)).arc((97,-83),(94,-77)).close().assemble().finalize().extrude(41).union(w0.sketch().segment((-100,-40),(-29,-40)).segment((-29,-98)).segment((-4,-98)).segment((-4,-40)).segment((34,-40)).segment((34,98)).segment((-100,98)).close().assemble().finalize().extrude(100))