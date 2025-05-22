import cadquery as cq
w0=cq.Workplane('YZ',origin=(-24,0,0))
w1=cq.Workplane('YZ',origin=(-24,0,0))
r=w0.sketch().arc((-82,-57),(0,-12),(43,-89)).arc((23,97),(-82,-57)).assemble().finalize().extrude(112).union(w1.sketch().segment((-87,-100),(87,-100)).segment((87,-10)).arc((1,-87),(-87,-10)).close().assemble().finalize().extrude(-65))