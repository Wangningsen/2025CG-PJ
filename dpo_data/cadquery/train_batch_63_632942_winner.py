import cadquery as cq
w0=cq.Workplane('YZ',origin=(-82,0,0))
r=w0.sketch().segment((-72,-100),(72,-100)).segment((72,-91)).arc((5,-23),(72,46)).segment((72,100)).segment((-72,100)).close().assemble().finalize().extrude(164)