import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((-19,8),(14,8)).arc((-3,15),(-19,8)).assemble().reset().face(w0.sketch().arc((17,-15),(19,-5),(17,4)).close().assemble()).finalize().extrude(200)