import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-56))
w1=cq.Workplane('ZX',origin=(0,1,0))
r=w0.sketch().segment((-49,48),(-49,83)).segment((5,83)).arc((-42,94),(-49,48)).assemble().reset().face(w0.sketch().arc((-16,-17),(12,-24),(38,-17)).close().assemble()).reset().face(w0.sketch().arc((49,-10),(62,23),(49,57)).close().assemble()).finalize().extrude(58).union(w1.sketch().push([(13,-20)]).circle(43).reset().face(w1.sketch().arc((-13,-34),(-3,-59),(0,-32)).arc((-5,-34),(-13,-34)).assemble(),mode='s').push([(13,-20)]).circle(18,mode='s').finalize().extrude(-101))