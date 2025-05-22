import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().arc((-68,-42),(0,-80),(68,-42)).close().assemble().reset().face(w0.sketch().segment((-68,42),(68,42)).arc((0,80),(-68,42)).assemble()).finalize().extrude(200)