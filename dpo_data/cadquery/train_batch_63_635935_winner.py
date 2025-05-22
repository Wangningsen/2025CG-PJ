import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-39))
w1=cq.Workplane('XY',origin=(0,0,-24))
r=w0.workplane(offset=79/2).moveTo(25,-63).cylinder(79,36).union(w1.sketch().segment((-98,16),(-90,16)).arc((-71,0),(-47,-3)).arc((-31,-1),(-18,8)).segment((-18,-18)).segment((100,-18)).segment((100,44)).segment((5,44)).arc((3,52),(1,59)).segment((1,76)).segment((-7,76)).arc((-48,99),(-90,76)).segment((-98,76)).segment((-98,59)).arc((-100,48),(-98,37)).close().assemble().finalize().extrude(-16))