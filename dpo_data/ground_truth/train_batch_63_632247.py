import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-11,0))
w1=cq.Workplane('XY',origin=(0,0,-31))
r=w0.sketch().segment((-43,12),(-8,12)).arc((29,-9),(66,12)).segment((100,12)).segment((100,57)).segment((66,57)).arc((29,78),(-8,57)).segment((-43,57)).close().assemble().push([(29,34)]).circle(26,mode='s').finalize().extrude(-21).union(w1.sketch().arc((-60,6),(-61,12),(-58,7)).arc((-70,31),(-60,6)).assemble().push([(-64,19)]).circle(7,mode='s').finalize().extrude(-69))