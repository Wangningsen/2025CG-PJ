import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-69,0))
w1=cq.Workplane('ZX',origin=(0,-41,0))
r=w0.sketch().segment((-53,-82),(-37,-82)).segment((-35,58)).segment((31,57)).segment((28,-82)).segment((53,-82)).segment((53,82)).segment((-53,82)).close().assemble().finalize().extrude(8).union(w1.sketch().arc((-99,-14),(-32,-26),(-32,-95)).arc((77,64),(-99,-14)).assemble().finalize().extrude(110))