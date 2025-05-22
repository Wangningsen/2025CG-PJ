import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,18,0))
r=w0.sketch().segment((-100,-2),(-78,-2)).segment((-68,-14)).segment((-57,-2)).segment((20,-2)).segment((20,71)).segment((-1,71)).segment((-10,82)).segment((-21,71)).segment((-100,71)).close().assemble().push([(42,-49.5)]).rect(116,65).finalize().extrude(-36)