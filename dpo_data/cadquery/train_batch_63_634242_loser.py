import cadquery as cq
w0=cq.Workplane('YZ',origin=(-30,0,0))
r=w0.sketch().segment((-91,-32),(-91,-18)).arc((-91,-49),(-62,-32)).close().assemble().reset().face(w0.sketch().segment((-16,8),(45,8)).arc((99,31),(42,33)).segment((-16,33)).close().assemble()).finalize().extrude(44).union(w0.workplane(offset=60/2).moveTo(-7,19.5).box(36,65,60))