import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,7,0))
r=w0.sketch().segment((-100,-10),(-79,-10)).arc((0,-79),(79,-10)).segment((100,-10)).segment((100,10)).segment((79,10)).arc((0,79),(-79,10)).segment((-100,10)).close().assemble().finalize().extrude(-14)