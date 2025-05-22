import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,55))
w1=cq.Workplane('XY',origin=(0,0,42))
r=w0.sketch().segment((-10,-84),(4,-90)).segment((4,-95)).segment((25,-95)).segment((25,-90)).arc((33,-87),(40,-84)).close().assemble().finalize().extrude(45).union(w1.workplane(offset=-142/2).moveTo(-19,74).cylinder(142,21))