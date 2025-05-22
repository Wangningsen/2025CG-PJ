import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-45,0))
r=w0.sketch().segment((-100,-97),(-21,-97)).segment((-21,-24)).arc((-60,-38),(-100,-25)).close().assemble().reset().face(w0.sketch().segment((36,82),(77,18)).segment((100,32)).segment((60,97)).close().assemble()).finalize().extrude(91)