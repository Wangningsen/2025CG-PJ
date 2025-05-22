import cadquery as cq
w0=cq.Workplane('YZ',origin=(-10,0,0))
w1=cq.Workplane('ZX',origin=(0,28,0))
r=w0.sketch().segment((-93,-51),(-49,-51)).segment((-49,-8)).segment((-93,-8)).segment((-93,-25)).arc((-100,-35),(-93,-44)).close().assemble().push([(19,-28)]).circle(33).push([(88,31)]).circle(12).finalize().extrude(-63).union(w1.workplane(offset=2/2).moveTo(41.5,71).box(39,4,2))