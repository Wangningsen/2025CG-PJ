import cadquery as cq
w0=cq.Workplane('YZ',origin=(-30,0,0))
r=w0.sketch().arc((-92,-18),(-88,-51),(-62,-32)).segment((-91,-32)).segment((-91,-20)).arc((-91,-19),(-92,-18)).assemble().reset().face(w0.sketch().segment((16,8),(44,8)).arc((100,25),(42,33)).segment((16,33)).close().assemble()).finalize().extrude(44).union(w0.workplane(offset=60/2).moveTo(-7,19.5).box(36,65,60))