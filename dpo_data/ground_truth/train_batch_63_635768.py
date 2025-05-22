import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,0,0))
r=w0.sketch().segment((-100,-15),(14,-15)).arc((95,-47),(25,4)).segment((25,71)).segment((-100,71)).close().assemble().finalize().extrude(-23).union(w0.sketch().arc((73,-61),(95,-26),(73,9)).segment((73,2)).arc((88,-26),(73,-53)).close().assemble().finalize().extrude(23))