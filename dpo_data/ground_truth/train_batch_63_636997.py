import cadquery as cq
w0=cq.Workplane('YZ',origin=(8,0,0))
w1=cq.Workplane('YZ',origin=(61,0,0))
r=w0.workplane(offset=-69/2).moveTo(32.5,85).box(39,30,69).union(w0.sketch().segment((-28,-27),(57,-27)).segment((57,50)).segment((49,50)).arc((45,48),(42,50)).segment((13,50)).arc((0,24),(-28,27)).close().assemble().finalize().extrude(-33)).union(w1.workplane(offset=-98/2).moveTo(-1.5,-58).box(111,84,98))