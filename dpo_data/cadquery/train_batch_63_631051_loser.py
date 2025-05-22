import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-42,0))
r=w0.workplane(offset=-58/2).moveTo(16,51).cylinder(58,40).union(w0.sketch().arc((-56,-91),(-40,-55),(-56,-19)).close().assemble().finalize().extrude(142))