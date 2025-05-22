import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-33))
r=w0.sketch().segment((-100,-34),(-23,-34)).segment((-23,-15)).arc((-62,-30),(-100,-15)).close().assemble().finalize().extrude(-24).union(w0.sketch().segment((10,-71),(100,-71)).segment((100,12)).segment((40,12)).arc((-42,55),(10,-22)).close().assemble().finalize().extrude(91))