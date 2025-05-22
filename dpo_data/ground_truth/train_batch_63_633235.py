import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-43))
r=w0.sketch().segment((-13,-11),(24,49)).arc((-76,69),(-13,-11)).assemble().reset().face(w0.sketch().segment((-13,-100),(36,-100)).segment((-13,-70)).close().assemble()).finalize().extrude(49).union(w0.workplane(offset=87/2).moveTo(52,36).box(64,128,87))