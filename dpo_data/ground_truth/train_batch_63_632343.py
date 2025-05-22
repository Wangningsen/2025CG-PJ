import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,3,0))
r=w0.sketch().push([(-27,24)]).circle(5).rect(4,6,mode='s').finalize().extrude(-38).union(w0.sketch().arc((-48,-70),(-33,-100),(-15,-72)).segment((-19,-70)).close().assemble().reset().face(w0.sketch().segment((4,95),(32,-24)).segment((52,-19)).segment((24,100)).close().assemble()).finalize().extrude(31))