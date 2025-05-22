import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-13))
w1=cq.Workplane('XY',origin=(0,0,-39))
r=w0.sketch().segment((15,46),(83,27)).segment((91,56)).segment((23,75)).close().assemble().push([(88,-6)]).circle(12).finalize().extrude(76).union(w1.sketch().arc((-88,-5),(-44,-72),(-54,6)).arc((-79,28),(-88,-5)).assemble().finalize().extrude(-24))