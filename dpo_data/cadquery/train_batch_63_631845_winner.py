import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-32,0))
w1=cq.Workplane('XY',origin=(0,0,24))
r=w0.sketch().segment((-62,-41),(-25,-100)).segment((-11,-92)).segment((-11,-97)).segment((10,-97)).segment((10,-78)).segment((62,-46)).segment((25,13)).segment((10,3)).segment((10,9)).segment((-11,9)).segment((-11,-9)).close().assemble().finalize().extrude(-31).union(w1.sketch().arc((0,-20),(97,-16),(30,55)).arc((-33,35),(0,-20)).assemble().push([(7,22)]).circle(11,mode='s').finalize().extrude(-35))