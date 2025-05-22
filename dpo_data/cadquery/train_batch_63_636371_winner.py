import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,5,0))
r=w0.workplane(offset=-59/2).moveTo(63.5,3).box(73,84,59).union(w0.sketch().push([(-80,-25)]).circle(20).reset().face(w0.sketch().segment((5,-22),(85,-22)).segment((85,2)).segment((38,2)).segment((38,-3)).segment((5,-3)).close().assemble()).finalize().extrude(49))