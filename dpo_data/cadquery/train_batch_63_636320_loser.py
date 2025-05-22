import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,62))
r=w0.sketch().segment((-100,-7),(-74,-7)).arc((-67,-20),(-55,-30)).arc((-55,9),(-30,49)).arc((-57,42),(-74,21)).segment((-100,21)).close().assemble().finalize().extrude(-124).union(w0.sketch().segment((62,-36),(79,-49)).segment((100,-22)).segment((62,3)).close().assemble().finalize().extrude(-5))