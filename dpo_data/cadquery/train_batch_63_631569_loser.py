import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-99))
w1=cq.Workplane('ZX',origin=(0,-60,0))
r=w0.sketch().segment((-100,-65),(100,-65)).segment((100,-12)).segment((15,-12)).segment((15,20)).segment((-14,20)).segment((-14,-12)).segment((-100,-12)).close().assemble().finalize().extrude(198).union(w1.sketch().segment((-18,23),(28,23)).arc((5,31),(-18,33)).close().assemble().finalize().extrude(125))