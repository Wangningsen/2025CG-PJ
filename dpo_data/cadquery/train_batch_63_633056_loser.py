import cadquery as cq
w0=cq.Workplane('YZ',origin=(26,0,0))
r=w0.workplane(offset=-90/2).moveTo(-59.5,-60).box(81,32,90).union(w0.sketch().arc((-10,11),(18,14),(40,0)).segment((100,0)).segment((100,76)).segment((-10,76)).close().assemble().finalize().extrude(38))