import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.workplane(offset=4/2).cylinder(4,21).union(w0.sketch().arc((-36,-3),(-29,-22),(-12,-34)).close().assemble().reset().face(w0.sketch().arc((-12,-34),(17,-31),(34,-10)).close().assemble()).reset().face(w0.sketch().segment((11,36),(36,-3)).arc((29,22),(11,36)).assemble()).finalize().extrude(200))