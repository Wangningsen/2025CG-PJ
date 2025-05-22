import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,18,0))
r=w0.workplane(offset=-104/2).moveTo(95,69).cylinder(104,5).union(w0.sketch().push([(-40.5,-3)]).rect(119,142).reset().face(w0.sketch().segment((-67,-27),(-67,21)).arc((-76,-3),(-67,-27)).assemble(),mode='s').reset().face(w0.sketch().arc((-15,-27),(-5,-3),(-15,21)).close().assemble(),mode='s').finalize().extrude(68))