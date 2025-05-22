import cadquery as cq
w0=cq.Workplane('YZ',origin=(41,0,0))
r=w0.workplane(offset=-83/2).moveTo(50,35).cylinder(83,50).union(w0.sketch().push([(-76,0)]).circle(24).reset().face(w0.sketch().segment((-88,-85),(-26,-85)).segment((-26,-30)).segment((-30,-30)).arc((-50,-54),(-81,-58)).segment((-81,-60)).segment((-88,-60)).close().assemble()).finalize().extrude(-11))