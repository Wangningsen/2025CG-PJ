import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-52))
r=w0.sketch().segment((88,30),(88,32)).segment((96,32)).segment((96,31)).arc((73,53),(95,30)).close().assemble().finalize().extrude(-23).union(w0.sketch().segment((-100,-58),(-56,-58)).arc((-62,-45),(-56,-32)).segment((-100,-32)).close().assemble().finalize().extrude(127))