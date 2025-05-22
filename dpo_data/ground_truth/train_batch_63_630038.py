import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-22,-52),(11,-55)).segment((22,52)).segment((-11,55)).close().assemble().finalize().extrude(-200)