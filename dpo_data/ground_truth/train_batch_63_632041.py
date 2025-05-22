import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-25,0))
r=w0.sketch().arc((43,14),(-100,-3),(44,-8)).arc((61,-5),(60,12)).arc((56,11),(56,15)).arc((49,17),(43,14)).assemble().finalize().extrude(-71).union(w0.sketch().segment((50,-44),(66,-44)).arc((32,50),(71,-42)).segment((71,-32)).arc((40,42),(50,-37)).close().assemble().finalize().extrude(121))