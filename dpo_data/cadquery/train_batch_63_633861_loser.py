import cadquery as cq
w0=cq.Workplane('YZ',origin=(73,0,0))
r=w0.sketch().arc((0,-74),(-27,-92),(4,-88)).arc((1,-81),(1,-74)).close().assemble().reset().face(w0.sketch().segment((-14,95),(2,7)).segment((30,12)).segment((15,100)).close().assemble()).push([(7,65)]).circle(4,mode='s').finalize().extrude(-146)