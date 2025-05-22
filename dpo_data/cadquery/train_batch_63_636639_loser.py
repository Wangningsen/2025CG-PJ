import cadquery as cq
w0=cq.Workplane('YZ',origin=(4,0,0))
w1=cq.Workplane('ZX',origin=(0,-11,0))
r=w0.workplane(offset=-32/2).moveTo(-29.5,-47.5).box(103,21,32).union(w0.sketch().segment((-81,-2),(-31,-39)).segment((-20,-24)).arc((71,73),(-52,30)).segment((-55,33)).close().assemble().finalize().extrude(-29)).union(w1.sketch().segment((-100,-7),(5,-7)).segment((5,19)).segment((-33,19)).arc((-48,28),(-64,19)).segment((-100,19)).close().assemble().finalize().extrude(-23))