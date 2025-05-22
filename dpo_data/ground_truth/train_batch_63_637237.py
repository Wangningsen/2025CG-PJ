import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,7))
w1=cq.Workplane('XY',origin=(0,0,3))
r=w0.workplane(offset=-107/2).moveTo(43,-31).cylinder(107,22).union(w0.workplane(offset=-38/2).moveTo(-22.5,44).box(85,32,38)).union(w1.sketch().segment((18,-60),(26,-60)).arc((21,-57),(18,-54)).close().assemble().finalize().extrude(97))