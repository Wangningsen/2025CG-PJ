import cadquery as cq
w0=cq.Workplane('YZ',origin=(-26,0,0))
r=w0.sketch().push([(-46,53)]).circle(47).push([(47.5,49)]).rect(3,30).finalize().extrude(7).union(w0.sketch().segment((52,-100),(67,-100)).segment((67,-95)).arc((93,-63),(67,-32)).segment((67,-25)).segment((52,-25)).segment((52,-32)).arc((28,-63),(52,-95)).close().assemble().push([(64,-56)]).circle(23,mode='s').finalize().extrude(53))