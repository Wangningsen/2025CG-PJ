import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,17))
r=w0.sketch().segment((-100,-28),(-87,-32)).segment((-61,53)).segment((-75,57)).close().assemble().push([(82.5,-55)]).rect(35,4).finalize().extrude(-35)