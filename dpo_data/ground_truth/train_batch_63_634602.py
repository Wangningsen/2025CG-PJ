import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,4,0))
r=w0.sketch().segment((45,69),(45,74)).arc((79,-4),(49,75)).segment((49,69)).close().assemble().finalize().extrude(-13).union(w0.workplane(offset=5/2).moveTo(-34,-10).cylinder(5,66))