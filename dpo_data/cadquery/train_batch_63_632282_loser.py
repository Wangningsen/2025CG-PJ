import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-31,0))
w1=cq.Workplane('YZ',origin=(-24,0,0))
r=w0.sketch().segment((-72,-7),(-67,-10)).segment((-67,-100)).segment((-57,-91)).arc((-55,-88),(-52,-83)).arc((18,-69),(34,1)).arc((49,91),(-32,39)).arc((-44,24),(-55,11)).segment((-57,12)).close().assemble().reset().face(w0.sketch().segment((4,-22),(6,-22)).segment((6,-18)).arc((5,-19),(4,-22)).assemble(),mode='s').finalize().extrude(97).union(w1.sketch().push([(-53,-18)]).rect(26,58).push([(-63,-16)]).circle(2,mode='s').push([(-37,-10)]).circle(4,mode='s').finalize().extrude(29))