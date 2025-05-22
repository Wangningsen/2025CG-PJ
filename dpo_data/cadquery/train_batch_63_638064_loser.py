import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-34))
r=w0.sketch().segment((-100,-34),(-22,-34)).segment((-22,-15)).arc((-61,-32),(-100,-15)).close().assemble().finalize().extrude(-24).union(w0.sketch().segment((10,-71),(100,-71)).segment((100,12)).segment((40,12)).arc((-41,56),(10,-22)).close().assemble().finalize().extrude(91))