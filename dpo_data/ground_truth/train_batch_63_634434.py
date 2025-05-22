import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().arc((-34,-18),(-3,-39),(31,-23)).close().assemble().reset().face(w0.sketch().segment((-31,23),(34,18)).arc((3,39),(-31,23)).assemble()).finalize().extrude(-200)