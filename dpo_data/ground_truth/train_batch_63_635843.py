import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-33,0))
r=w0.sketch().arc((-20,-53),(-54,-83),(-8,-84)).segment((56,-84)).segment((56,11)).segment((-20,11)).close().assemble().finalize().extrude(30).union(w0.sketch().segment((-47,-30),(36,-30)).arc((35,-27),(33,-25)).segment((33,11)).arc((32,91),(-44,68)).segment((-47,68)).close().assemble().finalize().extrude(67))