import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,59,0))
r=w0.sketch().arc((-4,-58),(-7,0),(23,31)).arc((-97,20),(-4,-58)).assemble().reset().face(w0.sketch().segment((11,-11),(37,-64)).segment((100,-33)).segment((73,23)).close().assemble()).finalize().extrude(-118)