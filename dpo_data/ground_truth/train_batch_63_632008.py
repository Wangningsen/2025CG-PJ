import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,64,0))
r=w0.sketch().push([(-51,32.5)]).rect(98,117).push([(56,-19)]).circle(44).finalize().extrude(-128).union(w0.sketch().segment((-63,62),(-53,64)).segment((-63,64)).close().assemble().push([(-3,-37)]).circle(54).finalize().extrude(-103))