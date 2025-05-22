import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-16,0))
r=w0.sketch().segment((-100,19),(-98,18)).segment((-91,24)).segment((-93,25)).close().assemble().finalize().extrude(1).union(w0.workplane(offset=21/2).moveTo(-39.5,-18).box(67,30,21)).union(w0.workplane(offset=32/2).moveTo(60,0).cylinder(32,40))