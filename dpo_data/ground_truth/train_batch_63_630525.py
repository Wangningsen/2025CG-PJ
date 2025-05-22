import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,53,0))
r=w0.sketch().arc((-99,-13),(-45,-19),(-15,-64)).arc((29,-25),(25,34)).segment((-53,34)).segment((-53,64)).arc((-90,35),(-99,-13)).assemble().reset().face(w0.sketch().segment((56,34),(90,13)).segment((100,30)).segment((94,34)).close().assemble()).finalize().extrude(-107)