import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().segment((-4,6),(-4,9)).arc((2,-9),(0,10)).segment((0,6)).close().assemble().finalize().extrude(-200)