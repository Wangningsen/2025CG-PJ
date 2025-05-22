import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,34,0))
w1=cq.Workplane('ZX',origin=(0,55,0))
r=w0.sketch().segment((-92,73),(-72,50)).segment((-40,76)).segment((-58,100)).close().assemble().finalize().extrude(-41).union(w1.sketch().segment((-20,-100),(92,-100)).segment((92,-23)).arc((85,-32),(76,-36)).arc((72,-38),(67,-39)).arc((66,-40),(65,-40)).segment((65,-63)).segment((50,-63)).segment((50,-40)).arc((35,-35),(23,-23)).segment((-20,-23)).close().assemble().finalize().extrude(-110))