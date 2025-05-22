import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,27,0))
w1=cq.Workplane('ZX',origin=(0,12,0))
r=w0.sketch().segment((35,-31),(100,-31)).segment((100,20)).arc((67,1),(35,20)).close().assemble().finalize().extrude(-64).union(w0.sketch().push([(-35,29)]).circle(65).push([(20,4)]).circle(7,mode='s').finalize().extrude(6)).union(w1.workplane(offset=24/2).moveTo(20,-67).cylinder(24,27))