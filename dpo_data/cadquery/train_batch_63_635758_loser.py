import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-98,0))
w1=cq.Workplane('XY',origin=(0,0,-79))
r=w0.workplane(offset=47/2).cylinder(47,88).union(w0.workplane(offset=198/2).box(98,62,198)).union(w1.sketch().segment((-18,-99),(-11,-99)).arc((0,-100),(11,-99)).segment((18,-99)).segment((18,-97)).arc((72,-28),(18,42)).segment((18,44)).segment((11,44)).arc((0,45),(-11,44)).segment((-18,44)).segment((-18,42)).arc((-72,-28),(-18,-97)).close().assemble().push([(-68,-46)]).circle(5,mode='s').finalize().extrude(122))