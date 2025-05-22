import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,58,0))
r=w0.sketch().arc((-5,-58),(-9,-8),(23,29)).arc((-97,20),(-5,-58)).assemble().reset().face(w0.sketch().segment((9,-8),(37,-64)).segment((100,-33)).segment((73,23)).close().assemble()).finalize().extrude(-117)