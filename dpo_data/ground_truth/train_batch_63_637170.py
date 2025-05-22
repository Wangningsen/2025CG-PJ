import cadquery as cq
w0=cq.Workplane('YZ',origin=(75,0,0))
r=w0.sketch().arc((-39,10),(-29,4),(-36,13)).arc((-34,8),(-39,10)).assemble().finalize().extrude(-149).union(w0.sketch().segment((-100,-20),(-33,-20)).arc((100,-8),(-26,35)).segment((-100,35)).close().assemble().push([(32,0)]).rect(72,112,mode='s').finalize().extrude(-85))