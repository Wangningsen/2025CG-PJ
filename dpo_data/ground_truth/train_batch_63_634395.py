import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-12))
w1=cq.Workplane('XY',origin=(0,0,-38))
r=w0.sketch().segment((15,46),(83,27)).segment((91,56)).segment((23,75)).close().assemble().push([(88,-6)]).circle(12).finalize().extrude(75).union(w1.sketch().arc((-87,-5),(-46,-73),(-54,6)).arc((-79,28),(-87,-5)).assemble().finalize().extrude(-24))