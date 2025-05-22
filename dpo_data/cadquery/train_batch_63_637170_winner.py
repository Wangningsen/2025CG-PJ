import cadquery as cq
w0=cq.Workplane('YZ',origin=(-10,0,0))
w1=cq.Workplane('YZ',origin=(-11,0,0))
r=w0.sketch().segment((-100,-19),(-34,-19)).arc((34,-68),(98,-16)).arc((100,1),(98,17)).arc((37,68),(-28,35)).segment((-100,35)).close().assemble().push([(32,0.5)]).rect(72,111,mode='s').finalize().extrude(84).union(w1.sketch().push([(-34,7)]).circle(6).push([(-33,5.5)]).rect(4,3,mode='s').finalize().extrude(-63))