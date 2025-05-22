import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,2,0))
r=w0.sketch().segment((-97,26),(-79,26)).arc((22,24),(-77,45)).segment((-97,45)).close().assemble().push([(38.5,-27.5)]).rect(9,47).push([(67,17)]).circle(30).finalize().extrude(-102).union(w0.workplane(offset=98/2).moveTo(25,-66).cylinder(98,16))