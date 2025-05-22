import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.workplane(offset=137/2).cylinder(137,69).union(w0.sketch().segment((-24,27),(2,27)).arc((-9,33),(-24,36)).close().assemble().reset().face(w0.sketch().arc((-24,44),(-13,53),(1,54)).arc((-13,54),(-24,44)).assemble()).finalize().extrude(200))