import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-42))
w1=cq.Workplane('ZX',origin=(0,-69,0))
r=w0.sketch().push([(-80,74)]).circle(10).reset().face(w0.sketch().segment((9,-84),(88,-84)).segment((88,37)).segment((69,37)).arc((47,2),(9,-19)).close().assemble()).finalize().extrude(142).union(w1.workplane(offset=91/2).moveTo(-79.5,49).box(41,68,91))