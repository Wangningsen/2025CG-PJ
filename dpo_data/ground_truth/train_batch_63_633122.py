import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,15,0))
w1=cq.Workplane('XY',origin=(0,0,-15))
r=w0.sketch().segment((-54,-16),(-24,-16)).arc((-43,24),(-24,63)).segment((-54,63)).close().assemble().finalize().extrude(-115).union(w0.sketch().arc((-8,-16),(3,-11),(10,-20)).arc((16,66),(-8,-16)).assemble().finalize().extrude(56)).union(w1.sketch().segment((-67,31),(-25,31)).segment((-25,-29)).segment((41,-29)).segment((41,55)).segment((22,55)).segment((22,100)).segment((-67,100)).close().assemble().finalize().extrude(16))