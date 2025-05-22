import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,4,0))
r=w0.sketch().segment((47,73),(47,74)).arc((54,-10),(52,75)).segment((52,73)).close().assemble().finalize().extrude(-13).union(w0.workplane(offset=5/2).moveTo(-34,-10).cylinder(5,66))