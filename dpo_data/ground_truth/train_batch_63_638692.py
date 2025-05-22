import cadquery as cq
w0=cq.Workplane('YZ',origin=(69,0,0))
r=w0.sketch().arc((-100,33),(4,8),(80,-68)).segment((100,-33)).segment((-80,68)).close().assemble().finalize().extrude(-139)