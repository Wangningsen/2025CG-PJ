import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,31))
r=w0.sketch().arc((-92,-11),(-68,-78),(-10,-38)).segment((-36,-56)).segment((-75,-10)).segment((-24,18)).segment((-36,24)).segment((-78,-15)).segment((-91,-10)).close().assemble().push([(50,22)]).rect(100,116).finalize().extrude(-62)