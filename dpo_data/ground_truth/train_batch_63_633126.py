import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-15,0))
w1=cq.Workplane('ZX',origin=(0,-45,0))
r=w0.sketch().segment((-22,-10),(86,-20)).segment((95,76)).segment((-12,87)).segment((-14,74)).arc((-95,62),(-17,35)).close().assemble().reset().face(w0.sketch().segment((-80,61),(-76,44)).segment((-26,54)).segment((-30,72)).close().assemble(),mode='s').reset().face(w0.sketch().segment((-88,-100),(-86,-100)).arc((-85,-98),(-85,-100)).segment((-55,-100)).segment((-55,-88)).segment((-88,-88)).close().assemble()).finalize().extrude(59).union(w1.workplane(offset=6/2).moveTo(35,11).cylinder(6,18))