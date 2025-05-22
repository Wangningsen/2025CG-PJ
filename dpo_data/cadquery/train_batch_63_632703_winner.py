import cadquery as cq
w0=cq.Workplane('YZ',origin=(88,0,0))
r=w0.sketch().arc((-100,-32),(5,-22),(100,34)).segment((-42,34)).close().assemble().finalize().extrude(-175)