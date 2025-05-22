import cadquery as cq
w0=cq.Workplane('YZ',origin=(-92,0,0))
r=w0.sketch().segment((-100,-2),(92,-2)).arc((-4,62),(-100,-2)).assemble().reset().face(w0.sketch().arc((98,-62),(100,-43),(98,-22)).close().assemble()).finalize().extrude(184)