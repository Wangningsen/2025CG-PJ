import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,3,0))
r=w0.sketch().push([(-52.5,73.5)]).rect(75,3).reset().face(w0.sketch().segment((-30,47),(-27,47)).segment((-27,48)).arc((-28,48),(-30,49)).close().assemble()).finalize().extrude(-103).union(w0.workplane(offset=97/2).moveTo(38,-29).box(104,92,97))