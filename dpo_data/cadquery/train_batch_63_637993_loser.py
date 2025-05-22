import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,57,0))
w1=cq.Workplane('ZX',origin=(0,67,0))
r=w0.workplane(offset=-130/2).moveTo(-50.5,-42).box(57,96,130).union(w0.sketch().segment((-98,-100),(-62,-100)).segment((-62,-32)).arc((-24,-54),(18,-38)).segment((20,-46)).segment((51,-39)).segment((47,-21)).arc((69,-7),(80,19)).arc((70,97),(11,47)).arc((6,37),(3,27)).arc((-43,18),(-63,-25)).segment((-63,-8)).segment((-98,-8)).close().assemble().finalize().extrude(-94)).union(w0.workplane(offset=16/2).moveTo(5,-14).cylinder(16,25)).union(w1.workplane(offset=-90/2).moveTo(-50,-80).box(56,4,90))