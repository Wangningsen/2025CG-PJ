import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-5,0))
w1=cq.Workplane('ZX',origin=(0,-18,0))
r=w0.sketch().push([(-17,-25)]).circle(42).circle(36,mode='s').finalize().extrude(-35).union(w0.sketch().push([(-35,38)]).circle(5).push([(68,35)]).circle(32).finalize().extrude(37)).union(w1.sketch().arc((-100,-7),(-91,2),(-81,6)).arc((-83,7),(-84,7)).arc((-86,5),(-87,7)).arc((-94,5),(-100,1)).close().assemble().finalize().extrude(58))