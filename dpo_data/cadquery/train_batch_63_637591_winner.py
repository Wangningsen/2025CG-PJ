import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().segment((-86,-78),(-59,-78)).segment((-50,-91)).segment((-86,28)).close().assemble().reset().face(w0.sketch().segment((-86,29),(-57,34)).segment((-56,36)).segment((-54,35)).segment((86,81)).arc((-4,82),(-57,34)).segment((-86,34)).close().assemble()).finalize().extrude(200)