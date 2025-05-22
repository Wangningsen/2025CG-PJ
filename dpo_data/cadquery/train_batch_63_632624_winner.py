import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((-29,35),(-18,19)).segment((15,19)).arc((-5,32),(-29,35)).assemble().reset().face(w0.sketch().arc((26,-35),(29,-16),(26,3)).close().assemble()).finalize().extrude(200)