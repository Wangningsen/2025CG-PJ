import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-1,0))
r=w0.workplane(offset=-54/2).moveTo(-51,27).box(28,12,54).union(w0.sketch().segment((-100,4),(3,-100)).segment((100,-5)).segment((-3,100)).close().assemble().push([(0,0)]).circle(22,mode='s').finalize().extrude(56))