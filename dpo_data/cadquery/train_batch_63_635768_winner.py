import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,0,0))
r=w0.sketch().segment((-100,-15),(15,-15)).arc((95,-47),(25,3)).segment((25,71)).segment((-100,71)).close().assemble().finalize().extrude(-23).union(w0.sketch().arc((73,-59),(95,-25),(73,9)).segment((73,0)).arc((88,-25),(73,-51)).close().assemble().finalize().extrude(23))