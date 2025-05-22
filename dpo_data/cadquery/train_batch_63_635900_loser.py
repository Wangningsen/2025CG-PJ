import cadquery as cq
w0=cq.Workplane('YZ',origin=(60,0,0))
r=w0.sketch().segment((-95,35),(15,-100)).segment((95,-35)).segment((-15,100)).close().assemble().reset().face(w0.sketch().segment((-31,68),(-20,46)).arc((-46,-19),(20,-48)).segment((27,-72)).segment((31,-68)).segment((21,-46)).arc((46,19),(-20,48)).segment((-27,72)).close().assemble(),mode='s').finalize().extrude(-120)