import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,10))
w1=cq.Workplane('XY',origin=(0,0,16))
r=w0.sketch().segment((-100,-34),(-85,-68)).segment((-42,-50)).segment((-57,-15)).close().assemble().finalize().extrude(-26).union(w0.sketch().segment((12,25),(12,31)).arc((-1,-19),(27,25)).close().assemble().finalize().extrude(5)).union(w1.sketch().segment((45,-1),(51,-5)).segment((100,64)).segment((94,68)).close().assemble().finalize().extrude(-32))