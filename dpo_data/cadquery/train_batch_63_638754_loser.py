import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,35,0))
w1=cq.Workplane('ZX',origin=(0,64,0))
r=w0.sketch().arc((5,15),(-24,-60),(54,-43)).segment((67,-48)).segment((100,49)).segment((25,75)).close().assemble().finalize().extrude(-99).union(w1.sketch().segment((-100,-31),(-78,-31)).arc((-61,-44),(-44,-31)).segment((-23,-31)).segment((-23,-20)).segment((-44,-20)).arc((-61,-7),(-78,-20)).segment((-100,-20)).close().assemble().finalize().extrude(-109))