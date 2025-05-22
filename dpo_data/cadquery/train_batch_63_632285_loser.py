import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-54,0))
w1=cq.Workplane('YZ',origin=(23,0,0))
r=w0.sketch().segment((18,-67),(61,-67)).segment((61,-52)).arc((100,0),(61,52)).segment((61,67)).segment((18,67)).segment((18,52)).arc((-19,0),(18,-52)).close().assemble().finalize().extrude(9).union(w1.workplane(offset=-61/2).moveTo(0,-22).cylinder(61,78))