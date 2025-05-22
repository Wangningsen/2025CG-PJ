import cadquery as cq
w0=cq.Workplane('YZ',origin=(9,0,0))
r=w0.sketch().segment((-67,-94),(-48,-94)).arc((-22,-100),(3,-94)).segment((20,-94)).segment((20,-81)).arc((25,-77),(29,-72)).arc((87,-15),(10,11)).arc((7,14),(3,16)).arc((-22,29),(-48,19)).segment((-67,19)).segment((-67,4)).arc((-89,-37),(-67,-78)).close().assemble().push([(38.5,81)]).rect(43,38).finalize().extrude(-19)