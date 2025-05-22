import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-73,0))
r=w0.sketch().segment((-52,-100),(52,-100)).segment((52,-9)).segment((-52,-9)).segment((-52,-97)).segment((-48,-97)).segment((-48,-99)).segment((-52,-99)).close().assemble().push([(-8,80)]).circle(20).finalize().extrude(80).union(w0.workplane(offset=147/2).moveTo(-27,36).cylinder(147,11))