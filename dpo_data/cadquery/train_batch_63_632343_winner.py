import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,4,0))
r=w0.sketch().push([(-27,24)]).circle(5).push([(-26,24)]).circle(2,mode='s').finalize().extrude(-38).union(w0.sketch().arc((-49,-70),(-32,-100),(-16,-70)).close().assemble().reset().face(w0.sketch().segment((3,95),(32,-24)).segment((52,-19)).segment((24,100)).close().assemble()).finalize().extrude(31))