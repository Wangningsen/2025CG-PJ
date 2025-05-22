import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,13,0))
w1=cq.Workplane('ZX',origin=(0,49,0))
r=w0.sketch().push([(-40,62)]).circle(38).circle(22,mode='s').finalize().extrude(-42).union(w0.sketch().push([(26,-64)]).rect(68,72).reset().face(w0.sketch().segment((-4,-87),(14,-87)).arc((0,-64),(14,-41)).segment((-4,-41)).close().assemble(),mode='s').reset().face(w0.sketch().arc((38,-41),(48,-52),(51,-66)).arc((26,-70),(45,-87)).segment((56,-87)).segment((56,-41)).close().assemble(),mode='s').finalize().extrude(36)).union(w1.workplane(offset=-98/2).moveTo(60,-34).cylinder(98,18))