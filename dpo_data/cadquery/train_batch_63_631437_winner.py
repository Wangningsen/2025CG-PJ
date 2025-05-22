import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-34))
r=w0.sketch().segment((40,59),(75,59)).segment((40,81)).arc((-24,68),(40,59)).assemble().finalize().extrude(-32).union(w0.sketch().arc((-33,-7),(-43,-98),(2,-18)).segment((13,-26)).segment((13,-25)).segment((-9,-11)).segment((-9,20)).segment((-33,20)).close().assemble().finalize().extrude(100))