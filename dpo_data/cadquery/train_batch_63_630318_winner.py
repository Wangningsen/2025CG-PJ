import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,50,0))
r=w0.sketch().segment((-39,-100),(90,-100)).segment((90,4)).segment((21,4)).arc((-51,96),(-39,-21)).close().assemble().finalize().extrude(-99).union(w0.sketch().segment((42,22),(45,17)).segment((45,22)).close().assemble().finalize().extrude(-28))