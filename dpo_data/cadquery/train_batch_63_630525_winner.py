import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,53,0))
r=w0.sketch().arc((-99,-13),(-44,-20),(-15,-64)).arc((30,-23),(25,34)).segment((-53,34)).segment((-53,64)).arc((-91,33),(-99,-13)).assemble().reset().face(w0.sketch().segment((56,34),(90,13)).segment((100,30)).segment((90,36)).segment((90,34)).close().assemble()).finalize().extrude(-107)