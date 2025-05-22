import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,73,0))
r=w0.workplane(offset=-147/2).moveTo(98,-61).cylinder(147,2).union(w0.sketch().arc((-100,-35),(-76,14),(-100,63)).close().assemble().reset().face(w0.sketch().arc((55,-57),(56,-56),(57,-56)).arc((21,13),(55,-57)).assemble()).finalize().extrude(-29))