import cadquery as cq
w0=cq.Workplane('YZ',origin=(36,0,0))
w1=cq.Workplane('YZ',origin=(36,0,0))
r=w0.sketch().arc((-72,-40),(-26,-98),(-36,-23)).segment((-36,20)).segment((-72,20)).close().assemble().push([(-18,86)]).circle(14).finalize().extrude(-68).union(w1.sketch().segment((63,-69),(78,-69)).arc((67,-49),(78,-30)).segment((63,-30)).close().assemble().finalize().extrude(-72))