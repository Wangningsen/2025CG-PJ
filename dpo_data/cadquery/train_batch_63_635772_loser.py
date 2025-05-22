import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,32))
r=w0.sketch().segment((-100,1),(17,-99)).segment((100,-1)).segment((41,50)).arc((2,-33),(-78,5)).arc((-81,10),(-82,16)).arc((-83,18),(-83,21)).close().assemble().reset().face(w0.sketch().segment((-22,91),(-5,90)).segment((-16,99)).close().assemble()).finalize().extrude(-64)