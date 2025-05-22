import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,8,0))
w1=cq.Workplane('XY',origin=(0,0,57))
r=w0.sketch().segment((-97,-61),(3,-61)).segment((3,-15)).arc((8,8),(3,30)).segment((3,77)).segment((-97,77)).segment((-97,30)).arc((-100,8),(-97,-15)).close().assemble().finalize().extrude(-98).union(w1.workplane(offset=43/2).moveTo(-24.5,25.5).box(105,129,43))