import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,3))
w1=cq.Workplane('ZX',origin=(0,-53,0))
r=w0.sketch().segment((-100,-31),(-72,-31)).arc((-51,-41),(-29,-31)).segment((-1,-31)).segment((-1,-22)).segment((80,-44)).segment((100,29)).segment((11,53)).segment((-1,7)).segment((-29,7)).arc((-51,17),(-72,7)).segment((-100,7)).close().assemble().finalize().extrude(34).union(w1.workplane(offset=71/2).moveTo(-6.5,-17).box(61,54,71))