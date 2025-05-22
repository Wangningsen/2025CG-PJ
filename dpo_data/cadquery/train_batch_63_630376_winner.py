import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,47,0))
r=w0.sketch().push([(-14,-59)]).rect(64,82).reset().face(w0.sketch().arc((-27,48),(12,3),(44,51)).segment((44,100)).segment((-27,100)).close().assemble()).finalize().extrude(-93)