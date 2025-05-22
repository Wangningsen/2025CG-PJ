import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().segment((-4,-10),(12,-10)).segment((12,9)).arc((-10,-11),(9,12)).segment((-4,12)).segment((-4,10)).arc((-7,1),(-4,-5)).close().assemble().finalize().extrude(-200)