import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,40))
r=w0.sketch().push([(-25.5,-59)]).rect(91,82).reset().face(w0.sketch().arc((17,20),(88,47),(25,88)).arc((-48,61),(17,20)).assemble()).finalize().extrude(-97).union(w0.sketch().arc((-88,-70),(-87,-72),(-86,-73)).segment((-87,-70)).close().assemble().finalize().extrude(17))