import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().segment((-86,-78),(-58,-78)).arc((-54,-85),(-50,-91)).segment((-86,22)).close().assemble().reset().face(w0.sketch().segment((-86,25),(-59,34)).segment((-86,34)).close().assemble()).reset().face(w0.sketch().segment((-58,34),(86,81)).arc((5,86),(-58,34)).assemble()).finalize().extrude(200)