import cadquery as cq
w0=cq.Workplane('YZ',origin=(-29,0,0))
r=w0.sketch().segment((-8,10),(-8,50)).arc((-37,-3),(11,-47)).arc((67,-35),(73,15)).segment((73,10)).close().assemble().finalize().extrude(-71).union(w0.sketch().segment((-77,16),(-73,16)).segment((-73,18)).arc((-75,19),(-77,19)).close().assemble().finalize().extrude(129))