import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-22,0))
w1=cq.Workplane('ZX',origin=(0,-6,0))
r=w0.sketch().segment((50,-1),(50,0)).segment((52,0)).arc((44,5),(50,-1)).assemble().finalize().extrude(-20).union(w0.sketch().arc((81,-100),(82,-99),(81,-97)).close().assemble().finalize().extrude(84)).union(w1.sketch().segment((-82,56),(-69,56)).arc((-64,14),(-22,2)).arc((50,22),(-6,66)).arc((-24,76),(-44,77)).segment((-44,100)).segment((-82,100)).close().assemble().finalize().extrude(-56))