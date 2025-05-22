import cadquery as cq
w0=cq.Workplane('YZ',origin=(35,0,0))
r=w0.sketch().segment((-100,8),(-64,8)).segment((-64,-93)).segment((-28,-93)).segment((-28,8)).segment((100,8)).segment((100,93)).segment((-100,93)).close().assemble().finalize().extrude(-69)