import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-14,0))
w1=cq.Workplane('ZX',origin=(0,-45,0))
r=w0.sketch().segment((-22,-10),(86,-20)).segment((95,76)).segment((89,77)).arc((87,76),(86,78)).segment((-12,88)).segment((-14,74)).arc((-94,68),(-17,35)).close().assemble().reset().face(w0.sketch().segment((-80,61),(-78,44)).segment((-26,54)).segment((-28,72)).close().assemble(),mode='s').push([(-71.5,-94)]).rect(33,12).finalize().extrude(59).union(w1.workplane(offset=6/2).moveTo(36,12).cylinder(6,17))