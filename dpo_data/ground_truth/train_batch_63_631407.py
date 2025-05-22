import cadquery as cq
w0=cq.Workplane('YZ',origin=(44,0,0))
r=w0.sketch().segment((32,47),(32,91)).segment((41,91)).arc((-64,-77),(82,57)).segment((82,47)).close().assemble().finalize().extrude(-88)