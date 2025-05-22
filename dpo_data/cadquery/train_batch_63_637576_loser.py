import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,23))
r=w0.sketch().segment((-78,-25),(-15,-25)).segment((-15,10)).arc((-73,63),(-78,-15)).close().assemble().push([(59,-31.5)]).rect(82,35).finalize().extrude(-46).union(w0.sketch().arc((33,-65),(37,-66),(40,-65)).close().assemble().finalize().extrude(-31))