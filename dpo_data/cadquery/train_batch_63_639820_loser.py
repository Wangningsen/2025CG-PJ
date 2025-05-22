import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,46))
w1=cq.Workplane('XY',origin=(0,0,20))
r=w0.sketch().segment((-81,34),(-52,34)).arc((-67,43),(-81,34)).assemble().finalize().extrude(-37).union(w1.sketch().arc((-46,-19),(42,-95),(43,24)).arc((-42,94),(-46,-19)).assemble().push([(16.5,-35.5)]).rect(61,53,mode='s').reset().face(w1.sketch().arc((56,-9),(68,-36),(60,-62)).segment((78,-62)).segment((78,-9)).close().assemble(),mode='s').finalize().extrude(-66))