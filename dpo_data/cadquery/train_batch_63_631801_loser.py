import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,57,0))
w1=cq.Workplane('ZX',origin=(0,83,0))
r=w0.workplane(offset=-140/2).moveTo(-3,-20).cylinder(140,35).union(w0.sketch().segment((-100,-68),(3,-68)).arc((84,45),(-41,-18)).segment((-100,-18)).close().assemble().push([(-13,-43)]).circle(11,mode='s').finalize().extrude(-44)).union(w1.sketch().push([(-3.5,-20)]).rect(31,62).push([(-17,-39)]).circle(2,mode='s').finalize().extrude(-111))