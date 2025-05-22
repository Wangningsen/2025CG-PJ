import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-57,0))
r=w0.sketch().segment((-85,58),(-69,31)).arc((-66,15),(-59,0)).segment((-59,-12)).segment((-52,-12)).segment((-52,100)).segment((-59,100)).segment((-59,86)).arc((-65,75),(-69,66)).close().assemble().reset().face(w0.sketch().segment((61,-39),(68,-100)).segment((85,-98)).segment((78,-37)).close().assemble()).finalize().extrude(114)