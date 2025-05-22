import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,0))
r=w0.sketch().push([(31,-10)]).circle(32).circle(27,mode='s').finalize().extrude(-92).union(w0.workplane(offset=-60/2).moveTo(31,-10).cylinder(60,46)).union(w0.sketch().push([(-33,56)]).circle(44).reset().face(w0.sketch().arc((23,-46),(60,-94),(26,-44)).segment((28,-55)).segment((25,-56)).close().assemble()).finalize().extrude(93))