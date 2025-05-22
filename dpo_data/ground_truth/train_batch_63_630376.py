import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,46,0))
r=w0.sketch().push([(-14.5,-59)]).rect(63,82).reset().face(w0.sketch().arc((-27,48),(10,3),(44,50)).segment((44,100)).segment((-27,100)).close().assemble()).finalize().extrude(-93)