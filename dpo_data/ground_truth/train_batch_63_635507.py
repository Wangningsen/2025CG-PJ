import cadquery as cq
w0=cq.Workplane('YZ',origin=(20,0,0))
w1=cq.Workplane('YZ',origin=(10,0,0))
r=w0.sketch().segment((-53,-85),(-39,-74)).segment((-19,-100)).arc((-8,15),(-47,-94)).close().assemble().reset().face(w0.sketch().segment((-12,86),(-5,30)).segment((28,34)).segment((21,90)).close().assemble()).finalize().extrude(-107).union(w0.workplane(offset=32/2).moveTo(70,-6).box(18,30,32)).union(w1.workplane(offset=77/2).moveTo(49,79).cylinder(77,21))