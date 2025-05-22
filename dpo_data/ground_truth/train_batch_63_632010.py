import cadquery as cq
w0=cq.Workplane('YZ',origin=(-80,0,0))
w1=cq.Workplane('ZX',origin=(0,28,0))
r=w0.sketch().segment((-11,2),(43,22)).arc((10,28),(-11,2)).assemble().reset().face(w0.sketch().arc((0,-27),(33,-33),(54,-7)).close().assemble()).finalize().extrude(-20).union(w0.sketch().arc((-48,-1),(37,-11),(-44,18)).arc((-53,10),(-48,-1)).assemble().finalize().extrude(180)).union(w1.workplane(offset=-15/2).moveTo(-5.5,-35).box(17,94,15))