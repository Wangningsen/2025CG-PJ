import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-51))
w1=cq.Workplane('XY',origin=(0,0,-46))
r=w0.sketch().arc((9,-98),(60,-64),(9,-31)).close().assemble().finalize().extrude(102).union(w1.sketch().segment((-60,7),(-42,7)).arc((-37,3),(-30,0)).segment((-30,89)).arc((-37,81),(-42,75)).segment((-60,75)).close().assemble().reset().face(w1.sketch().arc((-25,-9),(6,-18),(38,-9)).close().assemble()).reset().face(w1.sketch().arc((-25,91),(7,98),(38,91)).arc((6,100),(-25,91)).assemble()).finalize().extrude(74))