import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().arc((-92,100),(-88,70),(-83,40)).arc((31,-12),(92,-100)).segment((92,100)).close().assemble().finalize().extrude(200)