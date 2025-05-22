import cadquery as cq
w0=cq.Workplane('YZ',origin=(-15,0,0))
w1=cq.Workplane('YZ',origin=(-16,0,0))
r=w0.sketch().segment((-100,-19),(-9,-82)).segment((37,-15)).segment((-53,49)).close().assemble().push([(-31,-17)]).rect(40,18,mode='s').reset().face(w0.sketch().arc((21,60),(71,13),(86,82)).arc((56,58),(21,60)).assemble()).finalize().extrude(30).union(w1.sketch().segment((-5,-15),(-5,-14)).arc((-9,-19),(-4,-15)).close().assemble().finalize().extrude(4))