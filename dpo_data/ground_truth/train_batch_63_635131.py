import cadquery as cq
w0=cq.Workplane('YZ',origin=(-16,0,0))
r=w0.sketch().segment((-100,-19),(-10,-82)).segment((37,-15)).segment((-52,49)).close().assemble().push([(-31,-17)]).rect(40,18,mode='s').reset().face(w0.sketch().arc((21,60),(73,14),(86,82)).arc((58,59),(21,60)).assemble()).finalize().extrude(31)