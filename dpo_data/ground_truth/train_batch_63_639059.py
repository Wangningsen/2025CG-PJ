import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,65,0))
r=w0.workplane(offset=-147/2).moveTo(34,0).cylinder(147,66).union(w0.sketch().arc((-100,-3),(-54,-6),(-16,-32)).segment((-11,-16)).segment((-95,13)).close().assemble().finalize().extrude(17))