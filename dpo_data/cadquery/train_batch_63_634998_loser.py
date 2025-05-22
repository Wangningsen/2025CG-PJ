import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,28,0))
w1=cq.Workplane('ZX',origin=(0,37,0))
r=w0.sketch().segment((35,-31),(100,-31)).segment((100,20)).arc((68,1),(35,20)).close().assemble().finalize().extrude(-65).union(w0.workplane(offset=5/2).moveTo(-34,29).cylinder(5,66)).union(w1.workplane(offset=-26/2).moveTo(20,-67).cylinder(26,27))