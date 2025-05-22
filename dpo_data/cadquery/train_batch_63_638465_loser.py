import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,14))
w1=cq.Workplane('ZX',origin=(0,8,0))
r=w0.sketch().segment((8,0),(19,0)).segment((19,15)).arc((49,50),(19,85)).segment((19,100)).segment((8,100)).segment((8,85)).arc((-22,50),(8,15)).close().assemble().finalize().extrude(-21).union(w1.workplane(offset=-108/2).moveTo(0,-32).cylinder(108,17))