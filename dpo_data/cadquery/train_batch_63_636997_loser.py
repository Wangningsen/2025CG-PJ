import cadquery as cq
w0=cq.Workplane('YZ',origin=(8,0,0))
w1=cq.Workplane('YZ',origin=(61,0,0))
r=w0.workplane(offset=-69/2).moveTo(32.5,85).box(39,30,69).union(w0.sketch().segment((-28,-39),(57,-39)).segment((57,50)).segment((14,50)).arc((11,36),(2,25)).segment((2,21)).segment((-2,21)).arc((-14,19),(-28,21)).segment((-28,25)).arc((-35,18),(-28,10)).close().assemble().finalize().extrude(-33)).union(w1.workplane(offset=-98/2).moveTo(-1.5,-58).box(111,84,98))