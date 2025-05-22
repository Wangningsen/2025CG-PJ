import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,9,0))
w1=cq.Workplane('ZX',origin=(0,42,0))
r=w0.sketch().segment((-63,3),(-57,-13)).arc((-46,-7),(-35,-5)).segment((-41,12)).close().assemble().finalize().extrude(-2).union(w0.workplane(offset=27/2).moveTo(48,23).cylinder(27,52)).union(w1.workplane(offset=-85/2).moveTo(-50.5,-16.5).box(99,117,85))