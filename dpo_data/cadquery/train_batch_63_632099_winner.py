import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,10,0))
r=w0.sketch().segment((-53,-5),(-24,6)).segment((-19,25)).segment((-46,25)).close().assemble().finalize().extrude(-110).union(w0.sketch().arc((-2,-19),(26,-24),(44,-8)).segment((53,-8)).segment((53,-3)).close().assemble().finalize().extrude(90))