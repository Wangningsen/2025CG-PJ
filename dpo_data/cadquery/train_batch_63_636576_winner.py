import cadquery as cq
w0=cq.Workplane('YZ',origin=(-9,0,0))
r=w0.sketch().segment((-67,-94),(-50,-94)).arc((-25,-100),(0,-95)).segment((0,-94)).segment((20,-94)).segment((20,-82)).arc((25,-77),(29,-72)).arc((88,-18),(18,15)).arc((-22,29),(-60,12)).segment((-67,12)).segment((-67,6)).arc((-89,-37),(-67,-82)).close().assemble().push([(38.5,81)]).rect(43,38).finalize().extrude(18)