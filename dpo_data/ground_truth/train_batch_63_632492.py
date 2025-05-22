import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,34,0))
r=w0.sketch().segment((-88,100),(-83,92)).arc((-79,96),(-76,100)).close().assemble().finalize().extrude(-90).union(w0.sketch().arc((46,-37),(60,-100),(50,-36)).arc((49,-43),(46,-37)).assemble().finalize().extrude(23))