import cadquery as cq
w0=cq.Workplane('YZ',origin=(-6,0,0))
r=w0.sketch().segment((-42,-77),(25,-77)).segment((25,-61)).arc((35,-54),(44,-44)).arc((99,-6),(34,9)).arc((16,17),(-5,14)).segment((-30,14)).arc((-84,69),(-42,4)).close().assemble().finalize().extrude(12)