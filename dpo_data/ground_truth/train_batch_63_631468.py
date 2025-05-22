import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,50))
r=w0.sketch().arc((-63,-97),(26,-76),(63,8)).close().assemble().reset().face(w0.sketch().segment((-8,100),(62,16)).arc((39,68),(-8,100)).assemble()).finalize().extrude(-100)