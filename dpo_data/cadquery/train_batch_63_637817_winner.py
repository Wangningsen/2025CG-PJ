import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-14))
w1=cq.Workplane('XY',origin=(0,0,-29))
r=w0.sketch().arc((79,43),(-100,-5),(81,-38)).arc((100,5),(79,43)).assemble().reset().face(w0.sketch().segment((-32,-8),(-30,-8)).segment((-30,-62)).segment((60,-62)).segment((60,19)).segment((14,19)).arc((2,26),(-10,19)).segment((-30,19)).segment((-30,9)).close().assemble(),mode='s').finalize().extrude(43).union(w1.sketch().push([(61,3)]).circle(21).push([(61,3.5)]).rect(18,15,mode='s').finalize().extrude(42))