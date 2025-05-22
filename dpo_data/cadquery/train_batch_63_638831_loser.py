import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-90))
w1=cq.Workplane('ZX',origin=(0,-32,0))
r=w0.sketch().segment((-91,71),(2,71)).segment((2,64)).segment((35,64)).segment((35,65)).segment((37,65)).segment((37,64)).segment((47,64)).segment((47,94)).segment((-91,94)).close().assemble().push([(24,85)]).circle(9,mode='s').finalize().extrude(-10).union(w1.sketch().segment((-20,11),(-4,11)).arc((40,-13),(84,11)).segment((100,11)).segment((100,67)).segment((84,67)).arc((40,91),(-4,67)).segment((-20,67)).close().assemble().push([(-1.5,54.5)]).rect(7,15,mode='s').finalize().extrude(-62))