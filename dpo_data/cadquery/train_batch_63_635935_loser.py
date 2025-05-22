import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-39))
w1=cq.Workplane('XY',origin=(0,0,-24))
r=w0.workplane(offset=79/2).moveTo(25,-63).cylinder(79,36).union(w1.sketch().segment((-98,18),(-91,18)).arc((-55,-4),(-18,18)).segment((-18,-18)).segment((100,-18)).segment((100,44)).segment((4,44)).arc((4,56),(1,68)).segment((1,78)).segment((-6,78)).arc((-55,99),(-94,71)).segment((-98,71)).segment((-98,62)).arc((-100,48),(-98,34)).close().assemble().finalize().extrude(-16))