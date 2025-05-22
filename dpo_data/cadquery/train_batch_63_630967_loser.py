import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,21))
w1=cq.Workplane('XY',origin=(0,0,-14))
r=w0.sketch().arc((-10,-44),(-3,-37),(2,-27)).segment((7,-24)).segment((-10,-24)).close().assemble().push([(0.5,-4)]).rect(21,20).push([(77,50)]).circle(18).finalize().extrude(79).union(w1.sketch().segment((-95,-61),(-88,-61)).arc((-76,-68),(-65,-61)).segment((-57,-61)).segment((-57,-51)).segment((-65,-51)).arc((-76,-43),(-88,-51)).segment((-95,-51)).close().assemble().finalize().extrude(-86))