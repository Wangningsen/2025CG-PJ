import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,73,0))
r=w0.workplane(offset=-146/2).moveTo(98,-61).cylinder(146,2).union(w0.sketch().arc((-100,-35),(-76,14),(-100,63)).close().assemble().push([(39,-22)]).circle(39).finalize().extrude(-29))