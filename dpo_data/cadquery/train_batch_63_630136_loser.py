import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,42))
w1=cq.Workplane('XY',origin=(0,0,100))
r=w0.workplane(offset=-142/2).moveTo(-19,74).cylinder(142,21).union(w1.sketch().arc((-11,-84),(-5,-86),(2,-88)).segment((2,-95)).segment((25,-95)).segment((25,-88)).arc((33,-86),(40,-84)).close().assemble().finalize().extrude(-45))