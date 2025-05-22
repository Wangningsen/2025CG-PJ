import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-35))
w1=cq.Workplane('XY',origin=(0,0,-36))
r=w0.workplane(offset=54/2).moveTo(13,-11).cylinder(54,11).union(w1.sketch().segment((-100,-76),(56,-76)).segment((56,-61)).segment((100,-58)).segment((98,-30)).segment((56,-32)).segment((56,76)).segment((-100,76)).close().assemble().finalize().extrude(72))