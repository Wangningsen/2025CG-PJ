import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-25,0))
r=w0.sketch().arc((44,14),(-100,-1),(45,-6)).segment((64,-6)).segment((64,14)).close().assemble().finalize().extrude(-71).union(w0.sketch().push([(50,4)]).circle(50).circle(42,mode='s').finalize().extrude(121))