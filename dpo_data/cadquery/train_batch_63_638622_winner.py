import cadquery as cq
w0=cq.Workplane('YZ',origin=(-41,0,0))
w1=cq.Workplane('YZ',origin=(-68,0,0))
r=w0.sketch().segment((-100,1),(-16,-86)).segment((66,-8)).arc((100,19),(61,39)).segment((51,46)).arc((5,27),(-41,49)).segment((-43,46)).segment((-46,51)).close().assemble().finalize().extrude(108).union(w1.sketch().segment((-46,33),(-50,33)).arc((-7,-46),(36,33)).segment((36,35)).segment((35,35)).arc((14,53),(-12,57)).segment((-12,86)).segment((-46,86)).close().assemble().finalize().extrude(27))