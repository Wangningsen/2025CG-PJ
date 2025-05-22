import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,57))
w1=cq.Workplane('ZX',origin=(0,-90,0))
r=w0.workplane(offset=43/2).moveTo(-24.5,25.5).box(105,129,43).union(w1.sketch().segment((-97,-61),(3,-61)).segment((3,-13)).arc((8,7),(3,28)).segment((3,77)).segment((-97,77)).segment((-97,28)).arc((-100,7),(-97,-13)).close().assemble().finalize().extrude(98))