import cadquery as cq
w0=cq.Workplane('YZ',origin=(30,0,0))
w1=cq.Workplane('YZ',origin=(31,0,0))
r=w0.sketch().segment((-100,-1),(-76,-65)).segment((100,1)).segment((76,65)).close().assemble().finalize().extrude(-61).union(w1.sketch().arc((10,-33),(21,0),(10,33)).close().assemble().finalize().extrude(-11))