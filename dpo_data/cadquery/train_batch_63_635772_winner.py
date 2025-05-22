import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-31))
r=w0.sketch().segment((-100,1),(16,-99)).segment((100,-1)).segment((41,50)).arc((-14,-37),(-83,21)).close().assemble().reset().face(w0.sketch().arc((-22,91),(-14,91),(-5,90)).segment((-16,99)).close().assemble()).finalize().extrude(63)