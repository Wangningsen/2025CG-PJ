import cadquery as cq
w0=cq.Workplane('YZ',origin=(-24,0,0))
w1=cq.Workplane('YZ',origin=(-23,0,0))
r=w0.sketch().arc((-81,-57),(-7,-11),(43,-89)).arc((24,97),(-81,-57)).assemble().finalize().extrude(112).union(w1.sketch().segment((-87,-100),(87,-100)).segment((87,-11)).arc((0,-87),(-87,-11)).close().assemble().finalize().extrude(-65))