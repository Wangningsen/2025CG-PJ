import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-23))
r=w0.sketch().segment((-100,-34),(-56,-34)).arc((-52,-16),(-36,-6)).segment((-36,63)).segment((-100,63)).close().assemble().reset().face(w0.sketch().segment((-10,-63),(100,-63)).segment((100,61)).segment((-10,61)).segment((-10,-23)).arc((-7,-31),(-10,-39)).close().assemble()).finalize().extrude(46)