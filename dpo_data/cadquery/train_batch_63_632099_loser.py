import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,10,0))
r=w0.sketch().segment((-53,-5),(-24,6)).segment((-19,25)).segment((-46,25)).segment((-46,24)).close().assemble().finalize().extrude(-110).union(w0.sketch().arc((-2,-19),(23,-25),(44,-11)).segment((51,-8)).segment((53,-8)).segment((53,-4)).close().assemble().finalize().extrude(90))