import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,57))
r=w0.sketch().push([(-29.5,75.5)]).rect(73,49).reset().face(w0.sketch().segment((-5,-36),(-5,-27)).arc((24,-100),(42,-24)).segment((42,-36)).close().assemble()).push([(19,-13)]).circle(7).finalize().extrude(-115).union(w0.workplane(offset=-110/2).moveTo(31,-11).cylinder(110,35))