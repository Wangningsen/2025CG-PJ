import cadquery as cq
w0=cq.Workplane('YZ',origin=(68,0,0))
r=w0.sketch().segment((-98,-70),(10,-100)).arc((10,-71),(28,-48)).segment((-77,-48)).segment((-77,-25)).segment((40,-25)).segment((40,-43)).arc((61,-41),(80,-50)).segment((98,15)).segment((50,28)).segment((50,100)).segment((-88,100)).segment((-88,-25)).segment((-85,-25)).close().assemble().finalize().extrude(-137)