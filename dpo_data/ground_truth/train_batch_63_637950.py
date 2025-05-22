import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,6,0))
r=w0.sketch().segment((-100,-10),(-78,-10)).arc((1,-79),(79,-10)).segment((100,-10)).segment((100,10)).segment((79,10)).arc((1,79),(-78,10)).segment((-100,10)).close().assemble().finalize().extrude(-13)