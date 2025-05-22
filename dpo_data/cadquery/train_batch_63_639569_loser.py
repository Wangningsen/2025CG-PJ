import cadquery as cq
w0=cq.Workplane('YZ',origin=(42,0,0))
r=w0.workplane(offset=-83/2).moveTo(50,35).cylinder(83,50).union(w0.sketch().arc((-86,-20),(-66,-23),(-54,-7)).arc((-87,21),(-86,-20)).assemble().reset().face(w0.sketch().segment((-88,-85),(-26,-85)).segment((-26,-30)).segment((-40,-30)).arc((-58,-56),(-88,-58)).close().assemble()).finalize().extrude(-13))