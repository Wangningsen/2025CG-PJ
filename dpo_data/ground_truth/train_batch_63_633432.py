import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,19))
r=w0.sketch().push([(4,0)]).rect(56,142).reset().face(w0.sketch().segment((33,5),(100,5)).arc((85,12),(71,22)).arc((68,21),(68,25)).arc((61,32),(55,41)).segment((33,41)).close().assemble()).finalize().extrude(-75).union(w0.workplane(offset=37/2).moveTo(-43.5,8).box(113,82,37))