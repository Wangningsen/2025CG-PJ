import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-28))
w1=cq.Workplane('ZX',origin=(0,18,0))
r=w0.sketch().segment((-64,-22),(57,-74)).segment((100,28)).segment((-22,79)).close().assemble().finalize().extrude(117).union(w1.workplane(offset=-97/2).moveTo(-56.5,-29.5).box(65,141,97))