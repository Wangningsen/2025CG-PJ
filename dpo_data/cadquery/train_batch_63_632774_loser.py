import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,61,0))
r=w0.sketch().segment((63,-100),(70,-100)).segment((70,8)).arc((73,27),(70,46)).segment((70,60)).segment((65,60)).arc((-73,27),(63,-8)).close().assemble().finalize().extrude(-149).union(w0.sketch().arc((-10,21),(2,23),(13,22)).arc((2,27),(-10,21)).assemble().finalize().extrude(27))