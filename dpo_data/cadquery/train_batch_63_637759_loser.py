import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-15,0))
r=w0.sketch().segment((-61,-71),(-19,-71)).segment((-20,-66)).close().assemble().finalize().extrude(-85).union(w0.sketch().push([(-40,-19)]).circle(42).reset().face(w0.sketch().segment((-20,49),(-19,49)).arc((-1,64),(20,59)).arc((42,-30),(38,60)).segment((38,71)).segment((-20,71)).close().assemble()).finalize().extrude(115))