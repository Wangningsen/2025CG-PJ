import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-20))
w1=cq.Workplane('XY',origin=(0,0,27))
r=w0.sketch().push([(-94,-79)]).circle(6).reset().face(w0.sketch().segment((-31,-33),(-16,-33)).segment((-16,-24)).segment((-9,-24)).segment((-9,1)).segment((-12,1)).arc((-89,35),(-31,-30)).close().assemble()).finalize().extrude(-20).union(w0.sketch().arc((63,-6),(46,3),(67,0)).arc((-27,55),(63,-6)).assemble().finalize().extrude(39)).union(w1.sketch().push([(64.5,14)]).rect(71,64).push([(56,24.5)]).rect(38,3,mode='s').push([(78,29)]).circle(6,mode='s').finalize().extrude(13))