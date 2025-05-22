import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,35,0))
r=w0.sketch().push([(-84.5,-23.5)]).rect(31,115).reset().face(w0.sketch().segment((-8,9),(-6,9)).segment((-6,22)).arc((1,23),(7,26)).arc((16,33),(21,43)).arc((-25,74),(-8,22)).close().assemble()).push([(83,-51)]).circle(17).finalize().extrude(-70)