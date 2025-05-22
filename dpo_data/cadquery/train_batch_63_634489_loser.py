import cadquery as cq
w0=cq.Workplane('YZ',origin=(24,0,0))
r=w0.sketch().segment((-100,-6),(-68,-74)).segment((100,6)).segment((68,74)).close().assemble().finalize().extrude(-48)