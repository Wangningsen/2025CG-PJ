import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,59))
r=w0.workplane(offset=-119/2).moveTo(86.5,0).box(27,92,119).union(w0.sketch().segment((-100,20),(-97,20)).arc((-98,28),(-97,37)).segment((-100,37)).close().assemble().finalize().extrude(-77))