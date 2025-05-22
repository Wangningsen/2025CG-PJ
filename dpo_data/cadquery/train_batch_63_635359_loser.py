import cadquery as cq
w0=cq.Workplane('YZ',origin=(39,0,0))
r=w0.sketch().segment((-100,-44),(-76,-76)).segment((-36,-48)).arc((-26,-49),(-16,-55)).segment((-15,-55)).segment((-15,-56)).arc((95,30),(-45,19)).segment((-43,19)).segment((-48,-15)).segment((-56,-11)).arc((-60,-14),(-63,-17)).close().assemble().finalize().extrude(-78)