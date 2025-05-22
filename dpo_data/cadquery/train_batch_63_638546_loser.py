import cadquery as cq
w0=cq.Workplane('YZ',origin=(27,0,0))
w1=cq.Workplane('XY',origin=(0,0,28))
r=w0.sketch().arc((-33,-1),(-46,-82),(18,-30)).segment((-10,-46)).close().assemble().reset().face(w0.sketch().arc((-13,58),(-27,17),(13,-4)).arc((87,30),(22,82)).arc((17,77),(10,78)).arc((-4,70),(-13,58)).assemble()).finalize().extrude(-2).union(w0.sketch().segment((-8,16),(-7,15)).segment((-7,18)).close().assemble().reset().face(w0.sketch().segment((35,15),(37,15)).segment((37,18)).close().assemble()).finalize().extrude(73)).union(w1.workplane(offset=-10/2).moveTo(-60,-49).cylinder(10,40))