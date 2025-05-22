import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,24,0))
w1=cq.Workplane('ZX',origin=(0,63,0))
r=w0.sketch().segment((-51,-11),(-35,-100)).segment((59,-83)).segment((39,27)).segment((32,26)).arc((38,32),(44,34)).segment((84,34)).segment((84,77)).arc((85,80),(84,83)).segment((84,95)).segment((7,95)).segment((7,88)).arc((-76,73),(-51,-11)).assemble().finalize().extrude(-87).union(w1.sketch().segment((12,70),(85,70)).segment((85,93)).segment((12,93)).segment((12,76)).arc((15,75),(12,74)).close().assemble().finalize().extrude(-88))