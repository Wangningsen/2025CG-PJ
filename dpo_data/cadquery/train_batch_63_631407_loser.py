import cadquery as cq
w0=cq.Workplane('YZ',origin=(44,0,0))
r=w0.sketch().segment((32,47),(32,95)).arc((-56,-83),(83,56)).segment((83,47)).close().assemble().finalize().extrude(-88)