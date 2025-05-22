import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,32,0))
w1=cq.Workplane('XY',origin=(0,0,-33))
r=w0.sketch().push([(-43,-59)]).circle(41).circle(30,mode='s').push([(34,50)]).circle(50).finalize().extrude(-112).union(w1.sketch().arc((-46,44),(46,9),(-32,68)).segment((-26,68)).segment((-26,44)).close().assemble().push([(0,32)]).circle(4,mode='s').finalize().extrude(54))