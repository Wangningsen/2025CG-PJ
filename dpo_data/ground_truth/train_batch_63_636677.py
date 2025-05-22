import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-80,0))
w1=cq.Workplane('XY',origin=(0,0,-33))
r=w0.workplane(offset=20/2).moveTo(49,6).cylinder(20,4).union(w0.sketch().push([(-43,-59)]).circle(41).reset().face(w0.sketch().arc((-65,-40),(-29,-86),(-45,-30)).arc((-57,-30),(-65,-40)).assemble(),mode='s').push([(34,50)]).circle(50).finalize().extrude(112)).union(w1.sketch().arc((-47,44),(43,4),(-33,67)).segment((-26,67)).segment((-26,44)).close().assemble().push([(1,30.5)]).rect(10,5,mode='s').finalize().extrude(54))