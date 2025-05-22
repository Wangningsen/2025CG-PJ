import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,18,0))
r=w0.sketch().arc((-26,35),(-92,-43),(7,-16)).arc((-8,-14),(7,-11)).arc((-1,14),(-20,33)).arc((-8,66),(-26,35)).assemble().reset().face(w0.sketch().arc((68,-34),(98,-39),(77,-17)).arc((15,4),(68,-34)).assemble()).push([(84,-31)]).circle(7,mode='s').finalize().extrude(-58).union(w0.workplane(offset=22/2).moveTo(44,-11).cylinder(22,19))