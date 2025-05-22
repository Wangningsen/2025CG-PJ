import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-41))
w1=cq.Workplane('ZX',origin=(0,-17,0))
r=w0.sketch().segment((1,8),(4,8)).arc((30,-5),(57,8)).segment((60,8)).segment((60,14)).segment((40,14)).arc((15,23),(42,36)).segment((60,58)).segment((60,100)).segment((1,100)).segment((1,86)).close().assemble().finalize().extrude(-39).union(w1.sketch().segment((-11,-60),(80,-60)).segment((80,23)).segment((13,23)).arc((-18,27),(-11,-6)).close().assemble().push([(34,-20)]).circle(32,mode='s').finalize().extrude(-83))