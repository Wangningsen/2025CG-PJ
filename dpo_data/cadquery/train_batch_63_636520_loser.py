import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().segment((-15,-31),(15,-31)).segment((15,31)).arc((0,27),(-15,31)).close().assemble().finalize().extrude(200)