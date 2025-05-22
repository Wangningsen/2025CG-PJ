import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-5,0))
w1=cq.Workplane('ZX',origin=(0,-18,0))
r=w0.sketch().push([(-17,-25)]).circle(42).circle(36,mode='s').finalize().extrude(-35).union(w0.sketch().push([(-35,38)]).circle(5).push([(68,35)]).circle(32).finalize().extrude(37)).union(w1.sketch().arc((-100,-7),(-92,2),(-82,6)).segment((-100,6)).close().assemble().finalize().extrude(58))