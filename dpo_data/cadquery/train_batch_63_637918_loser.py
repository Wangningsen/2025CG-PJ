import cadquery as cq
w0=cq.Workplane('YZ',origin=(60,0,0))
r=w0.sketch().arc((-43,-12),(-41,12),(-43,37)).close().assemble().finalize().extrude(-120).union(w0.sketch().push([(-42,56.5)]).rect(116,85).push([(-1,-1)]).rect(34,92).push([(72,-71)]).circle(28).finalize().extrude(-70))