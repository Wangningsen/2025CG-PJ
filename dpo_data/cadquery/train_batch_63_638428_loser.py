import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((-59,-68),(59,-68)).segment((59,-58)).segment((-59,-14)).close().assemble().reset().face(w0.sketch().segment((-59,58),(59,14)).segment((59,68)).segment((-59,68)).close().assemble()).finalize().extrude(200)