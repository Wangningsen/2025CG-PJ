import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,4,0))
r=w0.sketch().push([(-27,24)]).circle(5).circle(4,mode='s').finalize().extrude(-39).union(w0.sketch().arc((-48,-70),(-33,-100),(-18,-70)).close().assemble().reset().face(w0.sketch().segment((4,95),(31,-24)).segment((52,-19)).segment((24,100)).close().assemble()).finalize().extrude(31))