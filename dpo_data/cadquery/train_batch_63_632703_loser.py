import cadquery as cq
w0=cq.Workplane('YZ',origin=(87,0,0))
r=w0.sketch().arc((-100,-32),(9,-20),(100,34)).segment((-42,34)).close().assemble().finalize().extrude(-174)