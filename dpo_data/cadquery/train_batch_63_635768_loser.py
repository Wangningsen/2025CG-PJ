import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-23,0))
r=w0.sketch().segment((-100,-15),(16,-15)).arc((95,-49),(25,3)).segment((25,71)).segment((-100,71)).close().assemble().finalize().extrude(23).union(w0.sketch().arc((73,-61),(95,-28),(73,6)).segment((73,-1)).arc((88,-28),(73,-54)).close().assemble().finalize().extrude(46))