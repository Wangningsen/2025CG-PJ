import cadquery as cq
w0=cq.Workplane('YZ',origin=(-26,0,0))
r=w0.sketch().push([(-46,53)]).circle(47).push([(47.5,50)]).rect(3,30).finalize().extrude(7).union(w0.sketch().segment((55,-100),(67,-100)).segment((67,-95)).arc((93,-62),(67,-30)).segment((67,-25)).segment((55,-25)).segment((55,-30)).arc((28,-62),(55,-95)).close().assemble().push([(65,-54)]).circle(24,mode='s').finalize().extrude(53))