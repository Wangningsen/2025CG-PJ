import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-54,0))
w1=cq.Workplane('YZ',origin=(-38,0,0))
r=w0.sketch().segment((16,-67),(62,-67)).segment((62,-56)).arc((100,0),(62,56)).segment((62,67)).segment((16,67)).segment((16,56)).arc((-22,0),(16,-56)).close().assemble().finalize().extrude(9).union(w1.workplane(offset=61/2).moveTo(0,-22).cylinder(61,78))