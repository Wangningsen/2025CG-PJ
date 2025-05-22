import cadquery as cq
w0=cq.Workplane('YZ',origin=(60,0,0))
r=w0.workplane(offset=-121/2).moveTo(-42,12.5).box(2,49,121).union(w0.sketch().push([(-42,56.5)]).rect(116,85).push([(-1,-2)]).rect(34,90).push([(72,-71)]).circle(28).finalize().extrude(-70))