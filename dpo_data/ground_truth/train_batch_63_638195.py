import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,21,0))
r=w0.sketch().segment((50,-84),(89,-94)).segment((100,-53)).segment((61,-43)).close().assemble().push([(66,-65.5)]).rect(2,23,mode='s').finalize().extrude(-43).union(w0.sketch().segment((-100,-11),(-42,-31)).segment((-25,19)).arc((1,83),(-63,59)).segment((-75,63)).close().assemble().finalize().extrude(-43))