import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().segment((-37,-7),(-1,-7)).arc((-7,0),(-1,7)).segment((-37,7)).close().assemble().reset().face(w0.sketch().segment((1,-7),(37,-7)).segment((37,7)).segment((1,7)).arc((7,0),(1,-7)).assemble()).finalize().extrude(200)