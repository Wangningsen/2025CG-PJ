import cadquery as cq
w0=cq.Workplane('YZ',origin=(-14,0,0))
r=w0.sketch().arc((-11,22),(-23,-99),(17,16)).arc((-2,0),(-11,22)).assemble().reset().face(w0.sketch().arc((55,100),(63,94),(71,100)).close().assemble()).finalize().extrude(27)