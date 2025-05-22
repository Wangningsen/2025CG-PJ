import cadquery as cq
w0=cq.Workplane('YZ',origin=(61,0,0))
r=w0.sketch().push([(-96,76)]).circle(4).push([(45,-27)]).circle(55).reset().face(w0.sketch().segment((87,70),(94,68)).segment((98,79)).segment((91,82)).close().assemble()).finalize().extrude(-122)