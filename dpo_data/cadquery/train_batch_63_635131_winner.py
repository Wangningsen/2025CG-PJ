import cadquery as cq
w0=cq.Workplane('YZ',origin=(16,0,0))
w1=cq.Workplane('YZ',origin=(15,0,0))
r=w0.sketch().segment((-100,-19),(-10,-82)).segment((38,-15)).segment((-52,49)).close().assemble().push([(-31,-17)]).rect(40,18,mode='s').reset().face(w0.sketch().arc((20,60),(76,15),(86,82)).arc((58,59),(20,60)).assemble()).finalize().extrude(-31).union(w1.sketch().arc((-51,-26),(-47,-27),(-43,-26)).close().assemble().finalize().extrude(-19))