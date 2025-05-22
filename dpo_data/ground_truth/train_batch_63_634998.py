import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,27,0))
w1=cq.Workplane('ZX',origin=(0,11,0))
r=w0.sketch().segment((35,-31),(100,-31)).segment((100,20)).arc((67,1),(35,20)).close().assemble().finalize().extrude(-64).union(w0.workplane(offset=6/2).moveTo(-35,29).cylinder(6,65)).union(w1.workplane(offset=25/2).moveTo(20,-67).cylinder(25,27))