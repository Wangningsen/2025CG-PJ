import cadquery as cq
w0=cq.Workplane('YZ',origin=(9,0,0))
w1=cq.Workplane('ZX',origin=(0,-28,0))
r=w0.workplane(offset=-72/2).moveTo(62,2).cylinder(72,38).union(w0.sketch().segment((-100,-59),(-57,-80)).segment((-32,-28)).segment((-75,-6)).close().assemble().push([(9,71)]).circle(9).reset().face(w0.sketch().arc((29,-14),(26,-5),(35,-7)).arc((1,19),(29,-14)).assemble()).finalize().extrude(19)).union(w1.sketch().push([(-14,8)]).circle(55).push([(-14,8.5)]).rect(88,39,mode='s').finalize().extrude(87))