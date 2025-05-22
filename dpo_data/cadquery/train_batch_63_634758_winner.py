import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().segment((-43,73),(-39,32)).arc((-5,50),(32,38)).segment((28,80)).close().assemble().reset().face(w0.sketch().segment((-32,-38),(-28,-80)).segment((43,-73)).segment((39,-32)).arc((5,-50),(-32,-38)).assemble()).finalize().extrude(-200)