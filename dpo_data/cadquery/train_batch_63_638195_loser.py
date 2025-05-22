import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,21,0))
r=w0.sketch().segment((-100,-11),(-42,-31)).segment((-25,19)).arc((-1,85),(-62,55)).segment((-75,63)).close().assemble().reset().face(w0.sketch().segment((50,-84),(89,-94)).segment((100,-53)).segment((61,-43)).close().assemble()).push([(67.5,-68.5)]).rect(5,29,mode='s').finalize().extrude(-43)