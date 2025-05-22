import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,55,0))
r=w0.workplane(offset=-110/2).moveTo(-51,27).box(28,12,110).union(w0.sketch().segment((-100,5),(3,-100)).segment((100,-5)).segment((-3,100)).close().assemble().circle(22,mode='s').finalize().extrude(-56))