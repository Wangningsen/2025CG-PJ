import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-32,0))
w1=cq.Workplane('XY',origin=(0,0,-11))
r=w0.sketch().segment((-62,-42),(-25,-100)).segment((-10,-91)).segment((-10,-97)).segment((10,-97)).segment((10,-78)).segment((62,-46)).segment((25,13)).segment((10,3)).segment((10,9)).segment((-10,9)).segment((-10,-10)).close().assemble().finalize().extrude(-31).union(w1.sketch().segment((-15,-15),(1,-15)).segment((1,-20)).segment((-6,-20)).arc((95,-22),(30,55)).arc((-29,43),(-15,-15)).assemble().push([(6,21)]).circle(12,mode='s').finalize().extrude(35))