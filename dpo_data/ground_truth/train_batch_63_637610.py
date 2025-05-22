import cadquery as cq
w0=cq.Workplane('YZ',origin=(-44,0,0))
w1=cq.Workplane('YZ',origin=(-28,0,0))
r=w0.workplane(offset=17/2).moveTo(50.5,-72).box(73,34,17).union(w0.sketch().segment((-13,-93),(13,-93)).segment((13,-79)).segment((-8,-79)).segment((-8,-27)).segment((24,-27)).arc((-16,-31),(-13,-71)).close().assemble().finalize().extrude(95)).union(w0.sketch().segment((-87,55),(-23,97)).arc((-66,92),(-87,55)).assemble().reset().face(w0.sketch().segment((-21,96),(10,50)).arc((2,78),(-21,96)).assemble()).finalize().extrude(130)).union(w1.workplane(offset=-58/2).moveTo(-52,-79).cylinder(58,21))