import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-25,0))
r=w0.sketch().arc((44,-10),(63,-2),(45,9)).arc((-100,0),(44,-10)).assemble().finalize().extrude(-71).union(w0.sketch().push([(50,4)]).circle(50).circle(42,mode='s').finalize().extrude(121))