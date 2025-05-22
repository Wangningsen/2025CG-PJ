import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,20))
r=w0.sketch().segment((-16,31),(62,18)).arc((-75,30),(61,48)).segment((-12,58)).close().assemble().push([(33,-68.5)]).rect(84,63).finalize().extrude(-41)