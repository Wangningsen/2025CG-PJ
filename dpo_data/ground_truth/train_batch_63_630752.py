import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,65,0))
r=w0.sketch().segment((-55,88),(-49,74)).arc((-36,81),(-22,86)).segment((-29,100)).close().assemble().reset().face(w0.sketch().segment((22,-86),(29,-100)).segment((55,-88)).segment((49,-74)).arc((36,-81),(22,-86)).assemble()).finalize().extrude(-129).union(w0.sketch().circle(48).circle(4,mode='s').finalize().extrude(-116))