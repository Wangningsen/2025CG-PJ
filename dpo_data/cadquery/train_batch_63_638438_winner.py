import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-2,0))
r=w0.sketch().segment((-24,-100),(24,-100)).segment((24,-17)).arc((30,0),(24,17)).segment((24,100)).segment((-24,100)).segment((-24,17)).arc((-30,0),(-24,-17)).close().assemble().finalize().extrude(5)