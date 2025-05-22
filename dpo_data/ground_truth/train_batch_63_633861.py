import cadquery as cq
w0=cq.Workplane('YZ',origin=(-73,0,0))
r=w0.sketch().arc((1,-70),(-30,-86),(5,-86)).arc((1,-79),(1,-70)).assemble().reset().face(w0.sketch().segment((-14,95),(-7,56)).segment((19,79)).segment((15,100)).close().assemble()).reset().face(w0.sketch().segment((-6,49),(2,7)).segment((30,12)).segment((20,72)).close().assemble()).finalize().extrude(146)