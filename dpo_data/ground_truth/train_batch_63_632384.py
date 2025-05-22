import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-15,0))
r=w0.sketch().segment((-100,-59),(-80,-59)).segment((-80,42)).arc((-90,46),(-100,52)).close().assemble().reset().face(w0.sketch().segment((-44,-43),(100,-43)).segment((100,59)).segment((-16,59)).arc((-29,48),(-44,42)).close().assemble()).push([(39,-25)]).circle(15,mode='s').push([(67,50)]).rect(4,10,mode='s').finalize().extrude(30)