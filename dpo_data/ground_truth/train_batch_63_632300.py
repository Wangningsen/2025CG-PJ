import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,50))
w1=cq.Workplane('XY',origin=(0,0,31))
r=w0.sketch().push([(-80,-0.5)]).rect(40,23).reset().face(w0.sketch().arc((-86,-3),(-84,-9),(-78,-7)).arc((-77,6),(-86,-3)).assemble(),mode='s').finalize().extrude(-100).union(w1.sketch().push([(45,0)]).circle(55).reset().face(w1.sketch().segment((-6,-12),(0,-12)).arc((45,-47),(90,-12)).segment((96,-12)).segment((96,12)).segment((90,12)).arc((45,47),(0,12)).segment((-6,12)).close().assemble(),mode='s').finalize().extrude(-22))