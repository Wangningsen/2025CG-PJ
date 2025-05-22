import cadquery as cq
w0=cq.Workplane('YZ',origin=(-57,0,0))
r=w0.sketch().segment((-53,81),(-33,81)).arc((-20,90),(-8,81)).segment((53,81)).segment((53,100)).segment((-53,100)).close().assemble().finalize().extrude(-28).union(w0.sketch().segment((1,-100),(18,-100)).segment((18,-4)).segment((3,-4)).arc((-46,3),(1,-11)).close().assemble().finalize().extrude(142))