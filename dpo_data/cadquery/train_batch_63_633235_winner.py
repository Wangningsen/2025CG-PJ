import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-43))
r=w0.sketch().arc((-4,88),(-77,14),(20,51)).arc((10,77),(-4,88)).assemble().reset().face(w0.sketch().segment((-13,-100),(36,-100)).arc((11,-85),(-13,-69)).close().assemble()).finalize().extrude(49).union(w0.workplane(offset=87/2).moveTo(52,36).box(64,128,87))