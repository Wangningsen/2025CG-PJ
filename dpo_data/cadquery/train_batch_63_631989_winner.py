import cadquery as cq
w0=cq.Workplane('YZ',origin=(-32,0,0))
w1=cq.Workplane('YZ',origin=(-18,0,0))
r=w0.sketch().segment((-67,30),(-1,-33)).segment((60,42)).segment((-14,100)).close().assemble().push([(8,-59.5)]).rect(98,81).finalize().extrude(7).union(w0.workplane(offset=64/2).moveTo(-2.5,15).box(95,76,64)).union(w1.workplane(offset=11/2).moveTo(40.5,-25).box(53,48,11))