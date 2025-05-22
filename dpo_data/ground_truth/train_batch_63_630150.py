import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,22,0))
r=w0.sketch().segment((-27,-55),(28,-55)).segment((28,-53)).segment((68,-76)).segment((100,-20)).segment((28,21)).segment((28,36)).segment((8,36)).arc((-94,46),(-27,-31)).close().assemble().finalize().extrude(-43)