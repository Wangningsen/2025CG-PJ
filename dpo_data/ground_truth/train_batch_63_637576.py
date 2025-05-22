import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,23))
r=w0.sketch().segment((-78,-25),(-15,-25)).segment((-15,10)).arc((-73,63),(-78,-15)).close().assemble().push([(59,-31.5)]).rect(82,35).finalize().extrude(-45).union(w0.workplane(offset=-31/2).moveTo(35,-65).cylinder(31,1))