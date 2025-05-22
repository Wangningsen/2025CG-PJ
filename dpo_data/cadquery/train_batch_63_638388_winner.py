import cadquery as cq
w0=cq.Workplane('YZ',origin=(14,0,0))
r=w0.sketch().arc((-12,22),(-13,-100),(18,16)).arc((7,0),(-12,22)).assemble().reset().face(w0.sketch().segment((55,94),(71,94)).segment((71,100)).segment((59,100)).arc((57,98),(55,99)).close().assemble()).finalize().extrude(-27)