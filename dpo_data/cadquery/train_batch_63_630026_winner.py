import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,10))
w1=cq.Workplane('YZ',origin=(-32,0,0))
r=w0.sketch().segment((-82,-91),(-22,-91)).segment((-22,-79)).arc((-4,-40),(-22,-1)).segment((-22,11)).segment((-82,11)).segment((-82,-1)).arc((-100,-40),(-82,-79)).close().assemble().push([(37,28)]).circle(63).finalize().extrude(-71).union(w0.sketch().segment((22,41),(38,41)).arc((32,48),(28,56)).segment((22,56)).close().assemble().finalize().extrude(39)).union(w1.workplane(offset=44/2).moveTo(32,33).cylinder(44,30))