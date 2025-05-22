import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-2))
w1=cq.Workplane('ZX',origin=(0,63,0))
r=w0.workplane(offset=-28/2).moveTo(61.5,-42).box(77,102,28).union(w0.workplane(offset=23/2).moveTo(-52.5,69.5).box(95,47,23)).union(w1.sketch().arc((-49,3),(49,-19),(-43,-61)).segment((15,-61)).segment((15,3)).close().assemble().finalize().extrude(-98))