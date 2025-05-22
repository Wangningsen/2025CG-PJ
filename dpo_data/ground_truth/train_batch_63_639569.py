import cadquery as cq
w0=cq.Workplane('YZ',origin=(41,0,0))
r=w0.workplane(offset=-83/2).moveTo(50,35).cylinder(83,50).union(w0.sketch().push([(-76,-1)]).circle(24).reset().face(w0.sketch().segment((-88,-85),(-52,-85)).arc((-51,-83),(-50,-85)).segment((-26,-85)).segment((-26,-30)).arc((-52,-54),(-88,-58)).close().assemble()).finalize().extrude(-12))