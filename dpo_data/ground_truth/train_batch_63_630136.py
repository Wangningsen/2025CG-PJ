import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,42))
w1=cq.Workplane('XY',origin=(0,0,55))
r=w0.workplane(offset=-142/2).moveTo(-19,74).cylinder(142,21).union(w1.sketch().arc((-10,-84),(-3,-87),(4,-89)).segment((4,-95)).segment((25,-95)).segment((25,-89)).arc((33,-87),(40,-84)).close().assemble().finalize().extrude(45))