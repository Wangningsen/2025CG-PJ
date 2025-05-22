import cadquery as cq
w0=cq.Workplane('YZ',origin=(-44,0,0))
w1=cq.Workplane('YZ',origin=(-28,0,0))
r=w0.workplane(offset=17/2).moveTo(45,-72).box(84,34,17).union(w0.sketch().segment((-13,-93),(13,-93)).segment((13,-79)).segment((-8,-79)).segment((-8,-27)).segment((23,-27)).arc((-15,-30),(-13,-69)).close().assemble().finalize().extrude(95)).union(w0.sketch().segment((-87,55),(-27,96)).segment((10,50)).arc((-38,100),(-87,55)).assemble().finalize().extrude(130)).union(w1.workplane(offset=-58/2).moveTo(-52,-79).cylinder(58,21))