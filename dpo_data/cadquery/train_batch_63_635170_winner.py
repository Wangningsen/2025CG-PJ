import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
w1=cq.Workplane('ZX',origin=(0,-66,0))
r=w0.sketch().segment((-88,40),(-1,-73)).segment((88,-7)).segment((30,65)).segment((-23,34)).segment((-44,73)).close().assemble().finalize().extrude(56).union(w1.sketch().arc((47,-32),(68,17),(47,65)).close().assemble().finalize().extrude(166))