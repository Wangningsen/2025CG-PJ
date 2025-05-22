import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,7))
r=w0.workplane(offset=-107/2).moveTo(43,-31).cylinder(107,22).union(w0.workplane(offset=-38/2).moveTo(-22.5,44).box(85,32,38)).union(w0.sketch().segment((18,-60),(26,-60)).segment((18,-54)).close().assemble().finalize().extrude(93))