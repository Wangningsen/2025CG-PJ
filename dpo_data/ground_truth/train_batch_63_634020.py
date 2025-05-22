import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-73,0))
r=w0.sketch().segment((-52,-100),(-48,-100)).arc((-46,-97),(-45,-100)).segment((52,-100)).segment((52,-9)).segment((-52,-9)).close().assemble().push([(-8,80)]).circle(20).finalize().extrude(81).union(w0.workplane(offset=147/2).moveTo(-27,36).cylinder(147,11))