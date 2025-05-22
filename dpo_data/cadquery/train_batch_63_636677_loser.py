import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,32,0))
w1=cq.Workplane('XY',origin=(0,0,-33))
r=w0.sketch().push([(-43,-59)]).circle(41).reset().face(w0.sketch().segment((-73,-70),(-69,-70)).arc((-43,-89),(-16,-70)).segment((-13,-70)).segment((-13,-53)).segment((-16,-53)).arc((-43,-30),(-69,-53)).segment((-73,-53)).close().assemble(),mode='s').push([(34,50)]).circle(50).finalize().extrude(-112).union(w1.sketch().arc((-50,28),(50,19),(-49,37)).arc((-48,33),(-50,28)).assemble().push([(0,31)]).circle(3,mode='s').finalize().extrude(54))