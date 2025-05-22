import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-31))
r=w0.workplane(offset=50/2).moveTo(28,23).box(54,24,50).union(w0.sketch().push([(-1,-82.5)]).rect(108,35).reset().face(w0.sketch().segment((23,98),(30,19)).segment((53,21)).segment((46,100)).close().assemble()).finalize().extrude(62))