import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,58,0))
r=w0.sketch().arc((-5,-57),(-4,4),(38,47)).arc((-95,25),(-5,-57)).assemble().reset().face(w0.sketch().segment((4,-4),(37,-63)).segment((100,-33)).segment((72,23)).close().assemble()).finalize().extrude(-117)