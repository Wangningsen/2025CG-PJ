import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-16))
w1=cq.Workplane('XY',origin=(0,0,9))
r=w0.sketch().segment((-100,-34),(-85,-68)).segment((-42,-50)).segment((-57,-15)).close().assemble().finalize().extrude(26).union(w0.sketch().segment((45,-1),(51,-5)).segment((100,64)).segment((94,68)).close().assemble().finalize().extrude(32)).union(w1.sketch().push([(10,6)]).circle(25).push([(9,23)]).circle(4,mode='s').finalize().extrude(6))