import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-61,0))
w1=cq.Workplane('ZX',origin=(0,-41,0))
r=w0.sketch().segment((-53,-82),(-37,-82)).segment((-36,-16)).segment((51,-19)).segment((51,-82)).segment((53,-82)).segment((53,82)).segment((-53,82)).close().assemble().finalize().extrude(-8).union(w1.sketch().arc((-99,-14),(-31,-27),(-32,-95)).arc((76,65),(-99,-14)).assemble().finalize().extrude(110))