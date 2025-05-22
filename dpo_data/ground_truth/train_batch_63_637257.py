import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,23,0))
w1=cq.Workplane('ZX',origin=(0,-15,0))
r=w0.sketch().segment((-51,16),(-26,2)).segment((2,50)).segment((-23,64)).close().assemble().push([(43,-56)]).circle(8).finalize().extrude(-111).union(w0.sketch().arc((5,-100),(14,-76),(6,-51)).close().assemble().finalize().extrude(-92)).union(w1.sketch().segment((22,69),(22,98)).segment((24,98)).arc((-4,75),(32,69)).close().assemble().finalize().extrude(103))