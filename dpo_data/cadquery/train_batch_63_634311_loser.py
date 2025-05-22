import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,40))
r=w0.sketch().push([(-25.5,-59)]).rect(91,82).reset().face(w0.sketch().arc((21,21),(88,49),(28,89)).arc((-48,62),(21,21)).assemble()).finalize().extrude(-97).union(w0.sketch().segment((-88,-73),(-86,-73)).segment((-86,-71)).arc((-87,-71),(-88,-73)).assemble().finalize().extrude(17))