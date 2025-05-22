import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-4,0))
r=w0.sketch().push([(-82,29)]).circle(18).rect(26,10,mode='s').finalize().extrude(-40).union(w0.sketch().push([(25,-25)]).rect(70,54).push([(8,-39)]).circle(10,mode='s').reset().face(w0.sketch().segment((46,23),(87,6)).segment((100,34)).segment((60,52)).close().assemble()).push([(73,28)]).circle(11,mode='s').finalize().extrude(48))