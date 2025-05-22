import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,35))
r=w0.sketch().segment((-100,-76),(56,-76)).segment((56,-61)).segment((100,-58)).segment((98,-29)).segment((56,-32)).segment((56,76)).segment((-100,76)).close().assemble().finalize().extrude(-71)