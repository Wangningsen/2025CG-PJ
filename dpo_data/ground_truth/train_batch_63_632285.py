import cadquery as cq
w0=cq.Workplane('YZ',origin=(23,0,0))
w1=cq.Workplane('ZX',origin=(0,-54,0))
r=w0.workplane(offset=-61/2).moveTo(0,-22).cylinder(61,78).union(w1.sketch().segment((18,-67),(61,-67)).segment((61,-56)).arc((100,0),(61,56)).segment((61,67)).segment((18,67)).segment((18,56)).arc((-20,0),(18,-56)).close().assemble().finalize().extrude(9))