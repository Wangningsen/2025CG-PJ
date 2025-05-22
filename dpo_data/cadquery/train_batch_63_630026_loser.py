import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,10))
w1=cq.Workplane('YZ',origin=(-32,0,0))
r=w0.sketch().segment((-82,-91),(-22,-91)).segment((-22,-79)).arc((-4,-40),(-22,-3)).segment((-22,11)).segment((-82,11)).segment((-82,-3)).arc((-100,-40),(-82,-79)).close().assemble().push([(37,28)]).circle(63).finalize().extrude(-72).union(w0.sketch().push([(28,32)]).circle(18).circle(2,mode='s').finalize().extrude(39)).union(w1.sketch().push([(32,32)]).circle(30).circle(20,mode='s').finalize().extrude(44))