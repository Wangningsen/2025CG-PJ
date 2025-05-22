import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,16,0))
r=w0.sketch().push([(-77.5,-53)]).rect(45,18).push([(-78,-53)]).circle(7,mode='s').reset().face(w0.sketch().segment((7,-16),(14,-16)).arc((15,-23),(17,-30)).segment((31,-32)).segment((30,-39)).segment((36,-40)).segment((37,-49)).arc((100,-15),(55,30)).segment((55,62)).segment((7,62)).close().assemble()).finalize().extrude(-32)