import cadquery as cq
w0=cq.Workplane('YZ',origin=(-55,0,0))
r=w0.sketch().segment((-90,-100),(90,-100)).segment((90,100)).segment((-72,100)).arc((-75,93),(-78,100)).segment((-90,100)).close().assemble().finalize().extrude(111)