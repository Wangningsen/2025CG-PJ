import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,22))
r=w0.sketch().segment((-78,-25),(-15,-25)).segment((-15,10)).arc((-73,63),(-78,-15)).close().assemble().push([(59,-31.5)]).rect(82,35).finalize().extrude(-45).union(w0.sketch().segment((35,-66),(36,-66)).segment((35,-64)).close().assemble().finalize().extrude(-28))