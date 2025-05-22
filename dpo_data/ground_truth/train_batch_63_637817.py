import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,13))
w1=cq.Workplane('XY',origin=(0,0,29))
r=w0.sketch().push([(60,3)]).circle(22).circle(8,mode='s').finalize().extrude(-42).union(w1.sketch().arc((83,36),(-100,-5),(86,-27)).arc((100,5),(83,36)).assemble().reset().face(w1.sketch().segment((-30,-62),(60,-62)).segment((60,19)).segment((14,19)).arc((-5,27),(-25,19)).segment((-30,19)).segment((-30,11)).arc((-32,0),(-30,-11)).close().assemble(),mode='s').finalize().extrude(-43))