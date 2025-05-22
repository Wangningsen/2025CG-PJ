import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-22,0))
r=w0.sketch().arc((-62,-18),(-57,-56),(-22,-43)).arc((-21,3),(-62,-18)).assemble().reset().face(w0.sketch().segment((-34,-22),(-25,-22)).segment((-25,-18)).arc((-29,-17),(-34,-16)).close().assemble(),mode='s').finalize().extrude(-9).union(w0.sketch().push([(-40,-65)]).circle(35).push([(7.5,76)]).rect(135,48).finalize().extrude(54))