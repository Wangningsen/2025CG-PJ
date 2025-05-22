import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
w1=cq.Workplane('ZX',origin=(0,-38,0))
r=w0.sketch().segment((-81,41),(-52,-64)).arc((-16,2),(-81,41)).assemble().finalize().extrude(-32).union(w1.sketch().segment((-100,49),(24,49)).segment((24,66)).segment((-10,66)).segment((-10,81)).segment((-67,81)).segment((-67,66)).segment((-100,66)).close().assemble().finalize().extrude(102))