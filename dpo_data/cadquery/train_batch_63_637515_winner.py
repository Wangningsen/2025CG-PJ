import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,2,0))
r=w0.sketch().segment((-97,26),(-79,26)).arc((22,31),(-77,45)).segment((-97,45)).close().assemble().push([(38.5,-20)]).rect(9,62).push([(67,18)]).circle(30).finalize().extrude(-102).union(w0.workplane(offset=98/2).moveTo(25,-65).cylinder(98,16))