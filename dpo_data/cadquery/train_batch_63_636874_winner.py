import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-8,0))
w1=cq.Workplane('ZX',origin=(0,-22,0))
r=w0.sketch().segment((-52,-100),(-50,-100)).segment((-50,-52)).arc((-38,-34),(-50,-16)).segment((-50,6)).segment((-52,6)).segment((-52,-15)).arc((-76,-34),(-52,-52)).close().assemble().push([(44,68)]).circle(32).finalize().extrude(92).union(w1.sketch().segment((-8,-58),(22,-58)).segment((22,16)).segment((70,16)).segment((70,21)).segment((17,21)).segment((17,18)).segment((-8,18)).close().assemble().finalize().extrude(-62))