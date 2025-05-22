import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
w1=cq.Workplane('ZX',origin=(0,-68,0))
r=w0.sketch().segment((-87,41),(0,-73)).segment((87,-8)).segment((31,65)).segment((-22,34)).segment((-43,73)).close().assemble().finalize().extrude(56).union(w1.sketch().arc((47,-32),(68,17),(47,65)).close().assemble().finalize().extrude(168))