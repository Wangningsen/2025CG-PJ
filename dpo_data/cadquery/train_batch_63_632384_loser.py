import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-15,0))
r=w0.sketch().push([(-90,-3.5)]).rect(20,111).reset().face(w0.sketch().segment((-44,-43),(100,-43)).segment((100,59)).segment((-14,59)).arc((-29,48),(-44,42)).close().assemble()).push([(38,-25)]).circle(15,mode='s').push([(68,49)]).circle(4,mode='s').finalize().extrude(30)