import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-97))
r=w0.sketch().segment((-100,-61),(-52,-61)).arc((0,-80),(52,-61)).segment((100,-61)).segment((100,61)).segment((52,61)).arc((0,80),(-52,61)).segment((-100,61)).close().assemble().finalize().extrude(194)