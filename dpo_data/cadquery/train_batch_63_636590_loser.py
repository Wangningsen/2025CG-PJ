import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,23))
r=w0.sketch().segment((-100,-34),(-56,-34)).arc((-50,-13),(-36,-1)).segment((-36,63)).segment((-100,63)).close().assemble().reset().face(w0.sketch().segment((-10,-63),(100,-63)).segment((100,61)).segment((-10,61)).segment((-10,-14)).arc((-7,-25),(-10,-40)).close().assemble()).finalize().extrude(-46)