import cadquery as cq
w0=cq.Workplane('YZ',origin=(-27,0,0))
r=w0.workplane(offset=-36/2).moveTo(6,23).cylinder(36,4).union(w0.sketch().arc((-7,46),(-6,-100),(18,44)).segment((18,100)).segment((-7,100)).close().assemble().finalize().extrude(91))