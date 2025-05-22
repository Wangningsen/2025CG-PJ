import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-42))
w1=cq.Workplane('YZ',origin=(15,0,0))
r=w0.workplane(offset=17/2).moveTo(48,-24).cylinder(17,34).union(w0.sketch().push([(-79,75)]).circle(9).reset().face(w0.sketch().segment((9,-84),(88,-84)).segment((88,37)).segment((69,37)).arc((50,2),(16,-18)).arc((14,-19),(13,-19)).arc((11,-19),(9,-18)).close().assemble()).finalize().extrude(142)).union(w1.workplane(offset=68/2).moveTo(-24,-79.5).box(90,41,68))