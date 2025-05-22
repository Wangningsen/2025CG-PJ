import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,21))
r=w0.workplane(offset=-66/2).moveTo(14,-55).cylinder(66,43).union(w0.sketch().arc((-66,-3),(-60,-14),(-51,-6)).arc((-34,97),(-66,-3)).assemble().push([(-45,45)]).circle(39,mode='s').reset().face(w0.sketch().segment((34,-4),(54,-51)).segment((100,-30)).segment((80,18)).close().assemble()).finalize().extrude(24))