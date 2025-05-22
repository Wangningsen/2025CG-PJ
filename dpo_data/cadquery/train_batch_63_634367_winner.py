import cadquery as cq
w0=cq.Workplane('YZ',origin=(-29,0,0))
r=w0.sketch().segment((-8,10),(-8,50)).arc((-37,-5),(14,-47)).arc((67,-35),(74,10)).close().assemble().finalize().extrude(-71).union(w0.sketch().arc((-77,17),(-75,15),(-75,16)).segment((-75,17)).segment((-76,18)).segment((-77,18)).arc((-76,17),(-77,17)).assemble().finalize().extrude(129))