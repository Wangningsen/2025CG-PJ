import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-34,0))
r=w0.sketch().arc((-20,-52),(-53,-86),(-7,-84)).segment((56,-84)).segment((56,11)).segment((-20,11)).close().assemble().finalize().extrude(31).union(w0.sketch().segment((-47,-30),(33,-30)).segment((33,11)).arc((35,88),(-44,67)).segment((-47,67)).close().assemble().finalize().extrude(67))