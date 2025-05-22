import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().segment((-14,27),(0,23)).arc((-7,26),(-14,27)).assemble().reset().face(w0.sketch().arc((-2,-27),(12,-11),(10,12)).close().assemble()).finalize().extrude(200)