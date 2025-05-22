import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,15,0))
w1=cq.Workplane('XY',origin=(0,0,-15))
r=w0.sketch().segment((-54,-16),(-24,-16)).arc((-43,24),(-24,63)).segment((-54,63)).close().assemble().finalize().extrude(-115).union(w0.workplane(offset=56/2).moveTo(10,24).cylinder(56,43)).union(w1.sketch().segment((-67,32),(-25,32)).segment((-25,-29)).segment((41,-29)).segment((41,32)).segment((43,32)).segment((43,34)).segment((41,34)).segment((41,38)).segment((22,38)).segment((22,100)).segment((-67,100)).close().assemble().finalize().extrude(16))