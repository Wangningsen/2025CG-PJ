import cadquery as cq
w0=cq.Workplane('YZ',origin=(-18,0,0))
r=w0.sketch().push([(-78,2)]).circle(22).push([(-78.5,2)]).rect(21,6,mode='s').finalize().extrude(11).union(w0.sketch().segment((68,-25),(94,-25)).segment((94,-14)).arc((100,0),(94,14)).segment((94,25)).segment((68,25)).segment((68,14)).arc((62,0),(68,-14)).close().assemble().finalize().extrude(36))