import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,49,0))
w1=cq.Workplane('ZX',origin=(0,13,0))
r=w0.workplane(offset=-98/2).moveTo(60,-34).cylinder(98,18).union(w0.sketch().push([(26,-64)]).rect(68,72).reset().face(w0.sketch().segment((0,-61),(14,-90)).segment((30,-81)).segment((16,-52)).close().assemble(),mode='s').push([(4,-43.5)]).rect(20,5,mode='s').push([(42,-64)]).circle(5,mode='s').push([(50,-56)]).circle(9,mode='s').finalize().extrude(-36)).union(w1.sketch().push([(-40,62)]).circle(38).circle(22,mode='s').finalize().extrude(-42))