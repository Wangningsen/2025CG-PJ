import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((-67,-6),(-10,-6)).arc((0,-12),(10,-6)).segment((67,-6)).segment((67,6)).segment((10,6)).arc((0,12),(-10,6)).segment((-67,6)).close().assemble().finalize().extrude(200)