import cadquery as cq
w0=cq.Workplane('YZ',origin=(56,0,0))
r=w0.sketch().segment((-90,-100),(90,-100)).segment((90,100)).segment((-71,100)).arc((-73,96),(-75,100)).segment((-90,100)).close().assemble().finalize().extrude(-111)