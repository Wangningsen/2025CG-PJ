import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().segment((-80,52),(19,-52)).segment((68,-6)).segment((-31,99)).close().assemble().finalize().extrude(-200).union(w0.sketch().segment((-30,-19),(7,-99)).segment((80,-65)).arc((60,-18),(77,30)).close().assemble().finalize().extrude(-168))