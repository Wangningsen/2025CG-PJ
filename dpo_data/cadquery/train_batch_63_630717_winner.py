import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-17,0))
w1=cq.Workplane('ZX',origin=(0,-37,0))
r=w0.workplane(offset=23/2).moveTo(-43,-37).cylinder(23,3).union(w0.sketch().push([(-8,37)]).circle(7).reset().face(w0.sketch().segment((6,42),(18,42)).segment((18,11)).segment((88,11)).segment((88,42)).segment((100,42)).segment((100,63)).segment((88,63)).segment((88,94)).segment((18,94)).segment((18,63)).segment((6,63)).close().assemble()).push([(53,52.5)]).rect(70,3,mode='s').finalize().extrude(79)).union(w1.workplane(offset=-25/2).moveTo(-43,-37).cylinder(25,57))