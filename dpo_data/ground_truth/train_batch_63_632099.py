import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,10,0))
r=w0.sketch().arc((-53,-5),(-39,2),(-24,5)).segment((-19,25)).segment((-46,25)).close().assemble().finalize().extrude(-110).union(w0.sketch().arc((-2,-19),(23,-25),(43,-9)).segment((53,-9)).segment((53,-4)).close().assemble().finalize().extrude(90))