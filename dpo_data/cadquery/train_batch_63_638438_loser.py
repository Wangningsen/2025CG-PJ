import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,3,0))
r=w0.sketch().segment((-24,-100),(24,-100)).segment((24,-18)).arc((30,0),(24,18)).segment((24,100)).segment((-24,100)).segment((-24,18)).arc((-30,0),(-24,-18)).close().assemble().finalize().extrude(-5)